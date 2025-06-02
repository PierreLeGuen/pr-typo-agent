"""GitHub API client and AI providers for PR Review Agent"""

import asyncio
import json
import logging
import re
from typing import Any, Dict, List, Optional

import aiohttp

logger = logging.getLogger(__name__)


class GitHubAPI:
    """Simple async GitHub API client"""

    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "PR-Review-Agent/1.0",
        }

    async def _request(
        self, method: str, url: str, data: Optional[Dict] = None
    ) -> Optional[Dict]:
        """Make HTTP request to GitHub API"""
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                    method,
                    url,
                    headers=self.headers,
                    json=data,
                    timeout=aiohttp.ClientTimeout(30),
                ) as response:
                    if response.status in [200, 201]:
                        return await response.json()
                    else:
                        logger.error(f"GitHub API error: {response.status}")
                        return None
            except Exception as e:
                logger.error(f"Request failed: {e}")
                return None

    async def get_open_prs(self, repo: str) -> List[Dict]:
        """Get open pull requests"""
        url = f"{self.base_url}/repos/{repo}/pulls?state=open"
        response = await self._request("GET", url)
        return response or []

    async def get_pr(self, repo: str, pr_number: int) -> Optional[Dict]:
        """Get specific pull request"""
        url = f"{self.base_url}/repos/{repo}/pulls/{pr_number}"
        return await self._request("GET", url)

    async def get_pr_files(self, repo: str, pr_number: int) -> List[Dict]:
        """Get files changed in PR"""
        url = f"{self.base_url}/repos/{repo}/pulls/{pr_number}/files"
        response = await self._request("GET", url)
        return response or []

    async def get_pr_comments(self, repo: str, pr_number: int) -> List[Dict]:
        """Get PR comments"""
        url = f"{self.base_url}/repos/{repo}/issues/{pr_number}/comments"
        response = await self._request("GET", url)
        return response or []

    async def post_comment(self, repo: str, pr_number: int, body: str) -> bool:
        """Post comment on PR"""
        url = f"{self.base_url}/repos/{repo}/issues/{pr_number}/comments"
        response = await self._request("POST", url, {"body": body})
        return response is not None

    async def post_review_comment(
        self, repo: str, pr_number: int, filename: str, line: int, body: str
    ) -> bool:
        """Post review comment on specific line"""
        # Get PR to get commit SHA
        pr = await self.get_pr(repo, pr_number)
        if not pr:
            return False

        url = f"{self.base_url}/repos/{repo}/pulls/{pr_number}/comments"
        data = {
            "body": body,
            "commit_id": pr["head"]["sha"],
            "path": filename,
            "line": line,
        }
        response = await self._request("POST", url, data)
        return response is not None


class AIProvider:
    """AI provider for code review"""

    def __init__(self, provider: str, api_key: str):
        self.provider = provider
        self.api_key = api_key

        if provider == "openai":
            import openai

            self.client = openai.AsyncOpenAI(api_key=api_key)
        elif provider == "anthropic":
            import anthropic

            self.client = anthropic.AsyncAnthropic(api_key=api_key)
        else:
            raise ValueError(f"Unsupported AI provider: {provider}")

    async def review_code(self, code: str, filename: str) -> List[Dict[str, Any]]:
        """Review code for quality issues"""
        prompt = f"""Review this code for quality, best practices, and potential issues:

File: {filename}

```
{code}
```

Focus on:
- Code quality and readability
- Performance issues
- Best practices violations
- Potential bugs

Respond with a JSON array of findings. Each finding should have:
- "type": "code_quality"
- "message": "Description of the issue"
- "line": line number (if applicable)
- "suggestion": "Suggested improvement" (if applicable)
"""

        try:
            if self.provider == "openai":
                response = await self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.1,
                    max_tokens=1500,
                )
                content = response.choices[0].message.content
            else:  # anthropic
                response = await self.client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1500,
                    temperature=0.1,
                    messages=[{"role": "user", "content": prompt}],
                )
                content = response.content[0].text

            # Try to parse JSON
            try:
                findings = json.loads(content)
                return findings if isinstance(findings, list) else []
            except json.JSONDecodeError:
                # Fallback: create a single finding
                return [
                    {
                        "type": "code_quality",
                        "message": "AI review completed",
                        "line": None,
                        "suggestion": None,
                    }
                ]

        except Exception as e:
            logger.error(f"AI review error: {e}")
            return []

    async def check_security(self, code: str, filename: str) -> List[Dict[str, Any]]:
        """Check code for security vulnerabilities"""
        prompt = f"""Analyze this code for security vulnerabilities:

File: {filename}

```
{code}
```

Look for:
- SQL injection
- XSS vulnerabilities
- Command injection
- Hardcoded secrets
- Insecure cryptography
- Input validation issues

Respond with JSON array of findings with:
- "type": "security"
- "message": "Description of security issue"
- "severity": "high"|"medium"|"low"
- "line": line number (if applicable)
- "suggestion": "How to fix"
"""

        try:
            if self.provider == "openai":
                response = await self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.1,
                    max_tokens=1500,
                )
                content = response.choices[0].message.content
            else:  # anthropic
                response = await self.client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1500,
                    temperature=0.1,
                    messages=[{"role": "user", "content": prompt}],
                )
                content = response.content[0].text

            try:
                findings = json.loads(content)
                return findings if isinstance(findings, list) else []
            except json.JSONDecodeError:
                return []

        except Exception as e:
            logger.error(f"Security check error: {e}")
            return []
