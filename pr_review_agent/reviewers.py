"""Review modules for PR Review Agent"""

import asyncio
import logging
import re
from typing import Any, Dict, List, Optional, Tuple, Union

logger = logging.getLogger(__name__)


class TypoReviewer:
    """LLM-based typo detection and correction"""

    def __init__(self, ai_provider: Optional[Any] = None):
        self.ai_provider = ai_provider

    async def review(self, files: List[Dict]) -> List[Dict[str, Any]]:
        """Check files for typos using LLM"""
        return await self._async_review(files)

    async def _async_review(self, files: List[Dict]) -> List[Dict[str, Any]]:
        """Async implementation of review"""
        findings = []

        for file_data in files:
            filename = file_data["filename"]

            # Skip non-text files
            if not self._should_check_file(filename):
                continue

            patch = file_data.get("patch", "")
            if not patch:
                continue

            # Extract added lines
            added_lines = self._extract_added_lines(patch)

            for line_num, line_content in added_lines:
                # Skip empty lines or lines with only symbols
                if not line_content.strip() or not any(
                    c.isalpha() for c in line_content
                ):
                    continue

                # Use LLM to check and correct the line
                if self.ai_provider:
                    corrected_line = await self._llm_spell_check(line_content)
                    if (
                        corrected_line
                        and corrected_line.strip() != line_content.strip()
                    ):
                        findings.append(
                            {
                                "type": "typo",
                                "file": filename,
                                "line": line_num,
                                "message": "Spelling/grammar corrections suggested",
                                "suggestion": corrected_line,
                                "severity": "low",
                            }
                        )
                else:
                    # Fallback to simple spell checking
                    corrected_line = self._simple_spell_check(line_content)
                    if (
                        corrected_line
                        and corrected_line.strip() != line_content.strip()
                    ):
                        findings.append(
                            {
                                "type": "typo",
                                "file": filename,
                                "line": line_num,
                                "message": "Possible typos detected",
                                "suggestion": corrected_line,
                                "severity": "low",
                            }
                        )

        return findings

    def _should_check_file(self, filename: str) -> bool:
        """Check if file should be spell-checked"""
        # Check for text files and code files with comments
        text_extensions = {".md", ".txt", ".rst", ".py", ".js", ".ts", ".html", ".css"}
        file_ext = "." + filename.split(".")[-1] if "." in filename else ""
        return file_ext.lower() in text_extensions

    def _extract_added_lines(self, patch: str) -> List[tuple]:
        """Extract added lines from patch"""
        added_lines = []
        current_line = 0

        for line in patch.split("\n"):
            if line.startswith("@@"):
                match = re.search(r"\+(\d+)", line)
                if match:
                    current_line = int(match.group(1))
            elif line.startswith("+") and not line.startswith("+++"):
                content = line[1:]
                added_lines.append((current_line, content))
                current_line += 1
            elif not line.startswith("-"):
                current_line += 1

        return added_lines

    async def _llm_spell_check(self, line: str) -> str:
        """Use LLM to check and correct spelling/grammar"""
        if not self.ai_provider:
            return line

        try:
            prompt = f"""Please check the following line for spelling and grammar errors and return the corrected version. 
If there are no errors, return the line exactly as is.
Only fix obvious typos and grammar mistakes. Do not change the meaning, style, or technical terms.

Line to check: {line}

Corrected line:"""

            if hasattr(self.ai_provider, "client"):
                # Use the async client from AIProvider
                if self.ai_provider.provider == "openai":
                    response = await self.ai_provider.client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=200,
                        temperature=0.1,
                    )
                    corrected = response.choices[0].message.content.strip()
                elif self.ai_provider.provider == "anthropic":
                    response = await self.ai_provider.client.messages.create(
                        model="claude-3-haiku-20240307",
                        max_tokens=200,
                        temperature=0.1,
                        messages=[{"role": "user", "content": prompt}],
                    )
                    corrected = response.content[0].text.strip()
                else:
                    return line
            else:
                return line

            # Clean up the response (sometimes LLMs add extra text)
            corrected = corrected.replace("Corrected line:", "").strip()
            if corrected.startswith('"') and corrected.endswith('"'):
                corrected = corrected[1:-1]

            return corrected if corrected else line

        except Exception as e:
            logger.error(f"LLM spell check error: {e}")
            return line

    def _simple_spell_check(self, line: str) -> str:
        """Simple fallback spell checking"""
        # Common typo corrections
        corrections = {
            "helo": "hello",
            "Helo": "Hello",
            "teh": "the",
            "adn": "and",
            "recieve": "receive",
            "occured": "occurred",
            "seperate": "separate",
        }

        corrected = line
        for typo, correction in corrections.items():
            if typo in corrected:
                corrected = corrected.replace(typo, correction)

        return corrected


class SecurityReviewer:
    """Simple security pattern detection"""

    async def review(self, files: List[Dict]) -> List[Dict[str, Any]]:
        """Check files for security issues"""
        findings = []

        for file_data in files:
            filename = file_data["filename"]
            patch = file_data.get("patch", "")

            if not patch:
                continue

            # Extract added lines
            current_line = 0
            for line in patch.split("\n"):
                if line.startswith("@@"):
                    match = re.search(r"\+(\d+)", line)
                    if match:
                        current_line = int(match.group(1))
                elif line.startswith("+") and not line.startswith("+++"):
                    content = line[1:]
                    issues = self._check_line_security(content, current_line)

                    for issue in issues:
                        issue["file"] = filename
                        findings.append(issue)

                    current_line += 1
                elif not line.startswith("-"):
                    current_line += 1

        return findings

    def _check_line_security(self, line: str, line_num: int) -> List[Dict[str, Any]]:
        """Check line for security issues"""
        findings: List[Dict[str, Any]] = []
        line_lower = line.lower().strip()

        if not line_lower or line_lower.startswith("#"):
            return findings

        # Check for hardcoded secrets
        secret_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
            r'api_key\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
        ]

        for pattern in secret_patterns:
            if re.search(pattern, line_lower):
                if not any(
                    placeholder in line_lower
                    for placeholder in ["example", "your_", "xxx"]
                ):
                    findings.append(
                        {
                            "type": "security",
                            "line": line_num,
                            "severity": "high",
                            "message": "Potential hardcoded secret detected",
                            "suggestion": "Use environment variables for secrets",
                        }
                    )
                    break

        # Check for SQL injection risks
        sql_keywords = ["select", "insert", "update", "delete"]
        if any(keyword in line_lower for keyword in sql_keywords):
            if any(pattern in line for pattern in [" + ", ".format(", "%"]):
                findings.append(
                    {
                        "type": "security",
                        "line": line_num,
                        "severity": "high",
                        "message": "Potential SQL injection vulnerability",
                        "suggestion": "Use parameterized queries",
                    }
                )

        # Check for command injection
        command_funcs = ["system(", "exec(", "os.system(", "subprocess."]
        if any(func in line_lower for func in command_funcs):
            if any(pattern in line_lower for pattern in ["input", "request", "user"]):
                findings.append(
                    {
                        "type": "security",
                        "line": line_num,
                        "severity": "high",
                        "message": "Potential command injection vulnerability",
                        "suggestion": "Validate and sanitize input",
                    }
                )

        # Check for weak crypto
        weak_algos = ["md5", "sha1", "des", "rc4"]
        if any(algo in line_lower for algo in weak_algos):
            findings.append(
                {
                    "type": "security",
                    "line": line_num,
                    "severity": "medium",
                    "message": "Weak cryptographic algorithm detected",
                    "suggestion": "Use stronger algorithms like SHA-256",
                }
            )

        return findings
