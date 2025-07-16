### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It monitors specified repositories for new pull requests and provides comprehensive feedback on code quality, potential security vulnerabilities, and typographical errors.

**Key Features:**

*   **Automated Code Review:** Leverages AI (OpenAI or Anthropic) to analyze code changes for quality, best practices, and potential issues.
*   **Typo and Grammar Detection:** Identifies and suggests corrections for spelling and grammar mistakes in new code and comments.
*   **Security Vulnerability Scanning:** Scans added code for common security risks such as hardcoded secrets, SQL injection, and command injection.
*   **Configurable Review Types:** Allows users to enable or disable specific review categories (typos, code quality, security) based on their needs.
*   **Automated Approval:** Can be configured to automatically approve pull requests where no issues are detected, streamlining the merge process.
*   **Scope Management:** Limits the review scope by configurable maximum files per PR and maximum lines per file to manage large changesets.
*   **Flexible Operation:** Can run continuously, monitoring multiple repositories, or be triggered to review a specific pull request on demand.
*   **GitHub Integration:** Posts detailed review comments directly on pull requests, including inline suggestions and a summary of findings.

**Inputs:**

*   **Environment Variables:** Configured via environment variables (or a `.env` file) for GitHub authentication, AI provider selection, review preferences, and repository monitoring.
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API access.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`: `true`/`false` to enable/disable typo review.
    *   `REVIEW_CODE_QUALITY`: `true`/`false` to enable/disable AI code quality review.
    *   `REVIEW_SECURITY`: `true`/`false` to enable/disable security review.
    *   `AUTO_APPROVE_MINOR`: `true`/`false` to enable/disable auto-approval for clean PRs.
    *   `MAX_FILES_PER_REVIEW`: Maximum files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
    *   `AGENT_NAME`: The name used by the bot in PR comments.
    *   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **Command Line Arguments (stdin):**
    *   `start`: Initiates continuous monitoring.
    *   `review <repo_url> <pr_number>`: Triggers a review for a specific pull request.
    *   `setup`: Guides interactive configuration setup.

**Outputs:**

*   **GitHub Comments:** Posts detailed comments on pull requests, including:
    *   Inline comments for specific code lines with issues, suggestions, and severity.
    *   A summary comment outlining all findings.
*   **GitHub Approvals:** Posts an approval comment if no issues are found and `AUTO_APPROVE_MINOR` is enabled.
*   **Console Logs (stdout):** Provides real-time status updates, warnings, and error messages during operation.