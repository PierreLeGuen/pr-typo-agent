### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It actively monitors specified repositories for new pull requests, performs comprehensive reviews, and provides feedback directly on GitHub.

**Main Functions:**

*   **Automated PR Monitoring:** Continuously checks designated GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Review:**
    *   **Typo and Grammar Detection:** Identifies and suggests corrections for spelling and grammar errors in code and documentation.
    *   **AI-Powered Code Quality Analysis:** Utilizes large language models (OpenAI or Anthropic) to assess code quality, adherence to best practices, potential bugs, and performance issues.
    *   **Security Vulnerability Scanning:** Detects common security flaws such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **GitHub Integration:** Posts inline comments for specific findings and a comprehensive summary comment on the pull request.
*   **Automated Approvals:** Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **On-demand Review:** Supports reviewing a specific pull request by providing its repository URL and PR number.

**Key Features:**

*   **Configurable Review Types:** Users can enable or disable typo, code quality, and security reviews independently.
*   **Review Scope Control:** Limits the number of files and lines reviewed per pull request to manage processing load.
*   **Flexible AI Provider:** Supports both OpenAI and Anthropic as AI backends for intelligent code analysis.
*   **Dry Run Mode:** Allows users to simulate reviews without posting actual comments to GitHub.
*   **Customizable Agent Name:** The name appearing on GitHub comments can be configured.

**Inputs:**

*   **Configuration (Environment Variables):**
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Choice of AI service ("openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Booleans to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean to enable/disable auto-approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `AGENT_NAME`: Name displayed in PR comments.
    *   `POLLING_INTERVAL`: Frequency of PR checks in seconds.
*   **GitHub Pull Requests:** New or updated pull requests in monitored repositories.
*   **CLI Arguments (for specific PR review):** Repository URL and Pull Request number.

**Outputs:**

*   **GitHub Comments:** Posts detailed inline comments on specific lines of code for identified issues (typos, code quality, security) and a summary comment for the entire pull request.
*   **GitHub Approvals:** Posts an approval comment if no issues are found (if configured).
*   **Console Logs:** Provides real-time status updates and error messages during operation.