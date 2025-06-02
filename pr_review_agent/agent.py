"""Main PR Review Agent - orchestrates the review process"""

import asyncio
import logging
import re
from typing import Any, Dict, List, Optional, Union

from .github_api import AIProvider, GitHubAPI
from .reviewers import SecurityReviewer, TypoReviewer

logger = logging.getLogger(__name__)


class PRReviewAgent:
    """Main agent that orchestrates PR reviews"""

    def __init__(
        self, config: Dict[str, Any], dry_run: bool = False, verbose: bool = False
    ):
        self.config = config
        self.dry_run = dry_run

        # Setup logging
        logging.basicConfig(
            level=logging.DEBUG if verbose else logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

        # Initialize components
        self.github = GitHubAPI(config["github_token"])

        # Initialize AI provider if code quality review is enabled
        self.ai: Optional[AIProvider] = None
        if config["review_code_quality"] and config["ai_provider"]:
            api_key = config.get(
                "openai_api_key"
                if config["ai_provider"] == "openai"
                else "anthropic_api_key"
            )
            if api_key:
                self.ai = AIProvider(config["ai_provider"], api_key)
            else:
                logger.warning("AI provider configured but no API key found")

        # Initialize reviewers
        self.reviewers: List[Union[TypoReviewer, SecurityReviewer]] = []
        if config["review_typos"]:
            self.reviewers.append(TypoReviewer(self.ai))
        if config["review_security"]:
            self.reviewers.append(SecurityReviewer())

    async def run(self):
        """Main run loop - monitor repositories for new PRs"""
        logger.info("🤖 PR Review Agent started")
        logger.info(
            f"Monitoring {len(self.config['watched_repositories'])} repositories"
        )

        if not self.config["watched_repositories"]:
            logger.warning("No repositories configured for monitoring")
            return

        while True:
            try:
                await self._check_repositories()
                await asyncio.sleep(self.config["polling_interval"])
            except KeyboardInterrupt:
                logger.info("Agent stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                await asyncio.sleep(60)

    async def _check_repositories(self):
        """Check all watched repositories for new PRs"""
        for repo in self.config["watched_repositories"]:
            try:
                logger.debug(f"Checking repository: {repo}")
                prs = await self.github.get_open_prs(repo)

                for pr in prs:
                    if await self._should_review_pr(repo, pr):
                        await self.review_pr(repo, pr)

            except Exception as e:
                logger.error(f"Error checking repository {repo}: {e}")

    async def _should_review_pr(self, repo: str, pr: Dict) -> bool:
        """Check if PR should be reviewed"""
        # Check if already reviewed
        comments = await self.github.get_pr_comments(repo, pr["number"])
        for comment in comments:
            if self.config["agent_name"] in comment.get("body", ""):
                logger.debug(f"PR #{pr['number']} already reviewed")
                return False

        # Skip draft PRs
        if pr.get("draft", False):
            logger.debug(f"Skipping draft PR #{pr['number']}")
            return False

        # Check PR size
        if pr.get("changed_files", 0) > self.config["max_files_per_review"]:
            logger.debug(f"PR #{pr['number']} too large")
            return False

        return True

    async def review_single_pr(self, repo_url: str, pr_number: int):
        """Review a specific PR"""
        # Extract repo name from URL
        repo = repo_url.replace("https://github.com/", "").replace(".git", "")

        logger.info(f"Reviewing PR #{pr_number} in {repo}")

        pr = await self.github.get_pr(repo, pr_number)
        if pr:
            await self.review_pr(repo, pr)
        else:
            logger.error(f"Could not fetch PR #{pr_number}")

    async def review_pr(self, repo: str, pr: Dict):
        """Review a pull request"""
        pr_number = pr["number"]
        logger.info(f"🔍 Reviewing PR #{pr_number}: {pr['title']}")

        try:
            # Get PR files
            files = await self.github.get_pr_files(repo, pr_number)
            if not files:
                logger.warning(f"No files found for PR #{pr_number}")
                return

            # Filter files
            filtered_files = self._filter_files(files)
            if not filtered_files:
                logger.info(f"No reviewable files in PR #{pr_number}")
                return

            # Run all reviews
            all_findings = []

            # Pattern-based reviews
            for reviewer in self.reviewers:
                logger.debug(f"Running {reviewer.__class__.__name__}")
                findings = await reviewer.review(filtered_files)
                all_findings.extend(findings)

            # AI-based code quality review
            if self.ai and self.config["review_code_quality"]:
                ai_findings = await self._ai_code_review(filtered_files)
                all_findings.extend(ai_findings)

            # Post results
            if all_findings:
                await self._post_review_comments(repo, pr_number, all_findings, pr)
            else:
                await self._post_approval_comment(repo, pr_number, pr)

        except Exception as e:
            logger.error(f"Error reviewing PR #{pr_number}: {e}")

    def _filter_files(self, files: List[Dict]) -> List[Dict]:
        """Filter files for review"""
        filtered = []

        ignore_patterns = [
            r"\.lock$",
            r"\.log$",
            r"\.bin$",
            r"\.exe$",
            r"\.dll$",
            r"node_modules/",
            r"\.git/",
            r"dist/",
            r"build/",
            r"__pycache__/",
        ]

        for file_data in files:
            filename = file_data["filename"]

            # Check ignore patterns
            if any(re.search(pattern, filename) for pattern in ignore_patterns):
                continue

            # Check file size
            if file_data.get("changes", 0) <= self.config["max_lines_per_file"]:
                filtered.append(file_data)

        return filtered

    async def _ai_code_review(self, files: List[Dict]) -> List[Dict[str, Any]]:
        """Run AI-powered code review"""
        if not self.ai:
            return []

        findings = []

        for file_data in files:
            filename = file_data["filename"]

            # Only review code files
            if not self._is_code_file(filename):
                continue

            patch = file_data.get("patch", "")
            if not patch:
                continue

            # Extract changed code
            changed_code = self._extract_changed_code(patch)
            if len(changed_code.strip()) < 10 or len(changed_code) > 3000:
                continue

            try:
                logger.debug(f"AI reviewing {filename}")
                ai_findings = await self.ai.review_code(changed_code, filename)

                for finding in ai_findings:
                    finding["file"] = filename
                    findings.append(finding)

            except Exception as e:
                logger.error(f"AI review error for {filename}: {e}")

        return findings

    def _is_code_file(self, filename: str) -> bool:
        """Check if file is a code file"""
        code_extensions = {
            ".py",
            ".js",
            ".ts",
            ".java",
            ".cpp",
            ".c",
            ".cs",
            ".php",
            ".rb",
            ".go",
        }
        file_ext = "." + filename.split(".")[-1] if "." in filename else ""
        return file_ext.lower() in code_extensions

    def _extract_changed_code(self, patch: str) -> str:
        """Extract changed code from patch"""
        lines = []
        for line in patch.split("\n"):
            if line.startswith("+") and not line.startswith("+++"):
                lines.append(line[1:])
            elif line.startswith(" "):
                lines.append(line[1:])
        return "\n".join(lines)

    async def _post_review_comments(
        self, repo: str, pr_number: int, findings: List[Dict], pr: Dict
    ):
        """Post review comments"""
        if self.dry_run:
            logger.info(f"[DRY RUN] Would post {len(findings)} review comments")
            for finding in findings:
                logger.info(f"  - {finding['type']}: {finding['message']}")
            return

        # Group by file and line
        file_comments: Dict[str, List[Dict]] = {}
        general_comments = []

        for finding in findings:
            if finding.get("file") and finding.get("line"):
                key = f"{finding['file']}:{finding['line']}"
                if key not in file_comments:
                    file_comments[key] = []
                file_comments[key].append(finding)
            else:
                general_comments.append(finding)

        # Post file-specific comments
        for file_line, comments in file_comments.items():
            filename, line = file_line.split(":", 1)
            comment_body = self._format_comments(comments)

            await self.github.post_review_comment(
                repo, pr_number, filename, int(line), comment_body
            )

        # Post summary comment
        summary = self._generate_summary(findings, pr)
        await self.github.post_comment(repo, pr_number, summary)

    async def _post_approval_comment(self, repo: str, pr_number: int, pr: Dict):
        """Post approval comment"""
        if self.dry_run:
            logger.info("[DRY RUN] Would post approval comment")
            return

        message = f"""## ✅ Review Complete

Hi @{pr['user']['login']}! I've reviewed this PR and found no issues. Great work! 🎉

**Review Summary:**
- No typos detected
- Code quality looks good
- No security concerns identified

---
*Review by {self.config['agent_name']}*
"""

        await self.github.post_comment(repo, pr_number, message)

    def _format_comments(self, comments: List[Dict]) -> str:
        """Format multiple comments"""
        formatted = []

        for comment in comments:
            emoji = {"typo": "✏️", "code_quality": "🔍", "security": "🔒"}.get(
                comment["type"], "💡"
            )
            formatted.append(
                f"{emoji} **{comment['type'].title()}**: {comment['message']}"
            )

            if comment.get("suggestion"):
                formatted.append(f"```suggestion\n{comment['suggestion']}\n```")

        return "\n\n".join(formatted)

    def _generate_summary(self, findings: List[Dict], pr: Dict) -> str:
        """Generate summary comment"""
        counts: Dict[str, int] = {}
        for finding in findings:
            finding_type = finding["type"]
            counts[finding_type] = counts.get(finding_type, 0) + 1

        summary = [f"## 🤖 PR Review Summary\n"]
        summary.append(f"Hi @{pr['user']['login']}! I've completed my review.\n")

        if findings:
            summary.append("**Issues Found:**")
            for finding_type, count in counts.items():
                emoji = {"typo": "✏️", "code_quality": "🔍", "security": "🔒"}.get(
                    finding_type, "💡"
                )
                summary.append(f"- {emoji} {finding_type.title()}: {count}")
            summary.append("\nPlease review the inline comments for details.")

        summary.append(f"\n---\n*Review by {self.config['agent_name']}*")

        return "\n".join(summary)
