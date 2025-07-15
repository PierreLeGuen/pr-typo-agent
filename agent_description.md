### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate code reviews on GitHub pull requests. It continuously monitors specified repositories for new PRs, performs comprehensive checks, and provides detailed feedback directly on GitHub.

**Main Functions:**
*   **Automated PR Monitoring:** Watches designated GitHub repositories for new or updated pull requests.
*   **Intelligent Code Review:** Conducts AI-powered analysis of code changes, focusing on:
    *   **Typo and Grammar Detection:** Identifies and suggests corrections for spelling and grammatical errors in code and comments.
    *   **Code Quality Assessment:** Evaluates code for best practices, readability, potential bugs, and performance issues.
    *   **Security Vulnerability Scanning:** Detects common security flaws such as hardcoded secrets, SQL injection risks, and command injection vulnerabilities.
*   **GitHub Integration:** Posts inline comments on specific lines of code for identified issues and provides a summarized review comment on the pull request.
*   **Conditional Approval:** Can be configured to automatically approve pull requests if no issues are found.
*   **Flexible AI Backend:** Supports both OpenAI and Anthropic models for AI-driven reviews.

**Key Features:**
*   Configurable review types (typos, code quality, security).
*   Ability to set limits on the number of files and lines reviewed per PR.
*   Customizable agent name for comments.
*   Supports dry-run mode for testing without posting comments.
*   Can review a single, specific pull request on demand.

**Configuration:**
The agent's behavior is controlled through environment variables, allowing for flexible setup without code changes. Key configurations include:
*   `GITHUB_TOKEN`: Your GitHub Personal Access Token for API authentication.
*   `AI_PROVIDER`: Specifies the AI service (e.g., `openai`, `anthropic`).
*   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
*   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
*   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Flags to enable/disable specific review types.
*   `AUTO_APPROVE_MINOR`: Enables automatic approval for clean PRs.
*   `POLLING_INTERVAL`: How often the agent checks for new PRs.

**Inputs:**
*   **GitHub Pull Requests:** Monitored via GitHub API polling.
*   **Environment Variables:** Configuration settings loaded at startup.
*   **Command Line Arguments:** Used for `start` or `review` commands (e.g., `repo_url`, `pr_number`).

**Outputs:**
*   **GitHub PR Comments:** Inline suggestions and a summary comment posted directly on the pull request.
*   **GitHub PR Approvals:** (Optional) An approval status posted if no issues are found.
*   **Console Logs:** Detailed operational logs for monitoring agent activity.