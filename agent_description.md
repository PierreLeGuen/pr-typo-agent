### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews based on configurable criteria.

**Main Functions:**
*   **Automated Pull Request Review:** Automatically reviews new pull requests in designated GitHub repositories.
*   **AI-Powered Code Analysis:** Utilizes AI models (OpenAI or Anthropic) to assess code quality, identify potential bugs, and suggest improvements.
*   **Security Vulnerability Detection:** Scans code for common security issues such as hardcoded secrets, SQL injection risks, and command injection vulnerabilities.
*   **Typo and Grammar Correction:** Checks for spelling and grammar errors in code comments, documentation, and string literals.
*   **Intelligent Commenting:** Posts detailed inline comments on specific lines of code where issues are found, and provides a summary comment for the entire pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Configurable Review Scope:** Allows setting limits on the number of files and lines reviewed per pull request to manage review complexity.

**Inputs:**
*   **Environment Variables:** Configured via environment variables (or a `.env` file) for authentication, AI provider selection, repository monitoring, and review settings.
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API access.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Booleans to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean to enable/disable auto-approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `AGENT_NAME`: The name used by the bot in comments.
    *   `POLLING_INTERVAL`: Frequency of checking for new PRs (in seconds).
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **GitHub API (HTTP):** Pull request details, file changes (diffs), and existing comments.
*   **Command Line (stdin):** For manual review of a specific PR, it takes `repository URL` and `pull request number`.

**Outputs:**
*   **GitHub Comments (HTTP):** Posts inline comments on specific lines of code and a summary comment on the pull request, detailing findings and suggestions.
*   **GitHub Pull Request Approvals (HTTP):** If configured, automatically approves pull requests that pass all reviews without issues.
*   **Console/Log Output (stdout):** Provides real-time status updates, warnings, and error messages during operation.