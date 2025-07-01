### PR Review Agent

**Description:**
The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests, performs comprehensive reviews covering code quality, potential security vulnerabilities, and typographical errors, and then provides detailed feedback directly on the pull request. It can also be configured to automatically approve clean pull requests.

**Key Features:**
*   **Automated PR Monitoring:** Watches designated GitHub repositories for new or updated pull requests.
*   **Multi-faceted Review:** Conducts reviews for:
    *   **Typographical and Grammar Errors:** Identifies and suggests corrections for typos and grammatical issues in code comments, documentation, and string literals, optionally leveraging AI.
    *   **AI-Powered Code Quality:** Utilizes large language models (LLMs) from providers like OpenAI or Anthropic to assess code quality, adherence to best practices, and potential bugs.
    *   **Security Vulnerability Detection:** Scans for common security patterns such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **GitHub Integration:** Posts inline comments for specific findings and a comprehensive summary comment on the pull request.
*   **Configurable Behavior:** Allows users to enable/disable specific review types, set limits on file/line review sizes, and configure automatic approvals for clean PRs.
*   **Flexible AI Provider:** Supports both OpenAI and Anthropic as AI backends for intelligent reviews.
*   **On-Demand Review:** Can be triggered to review a specific pull request manually via command line.

**Inputs:**
*   **GitHub API (HTTP):** Receives pull request data (details, files, diffs, existing comments) from monitored repositories.
*   **Environment Variables:** Configuration settings for GitHub authentication, AI provider details, review preferences, and monitored repositories.
*   **Command Line Arguments (stdin):** For manual review of a specific PR (repository URL, pull request number).

**Outputs:**
*   **GitHub PR Comments (HTTP):** Posts new comments on pull requests, including:
    *   Inline comments for specific issues (typos, code quality, security).
    *   A summary comment detailing all findings.
    *   An approval comment if no issues are found and auto-approval is enabled.
*   **Console Logs (stdout):** Provides real-time status updates, errors, and debugging information.

**Configuration (Environment Variables):**
*   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
*   `AI_PROVIDER`: Specifies the AI service provider ("openai" or "anthropic").
*   `OPENAI_API_KEY`: API key for OpenAI (if `AI_PROVIDER` is "openai").
*   `ANTHROPIC_API_KEY`: API key for Anthropic (if `AI_PROVIDER` is "anthropic").
*   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
*   `REVIEW_TYPOS`: `true` or `false` to enable/disable typo review.
*   `REVIEW_CODE_QUALITY`: `true` or `false` to enable/disable AI code quality review.
*   `REVIEW_SECURITY`: `true` or `false` to enable/disable security review.
*   `AUTO_APPROVE_MINOR`: `true` or `false` to automatically approve PRs with no issues.
*   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
*   `MAX_LINES_PER_FILE`: Maximum lines per file to review.
*   `AGENT_NAME`: The name used for comments posted by the agent.
*   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.
*   `MAX_RETRIES`: Maximum retries for API calls.
*   `GITHUB_WEBHOOK_SECRET`: Optional secret for GitHub webhook validation.