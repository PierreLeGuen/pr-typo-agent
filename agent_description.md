### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories, applies various review checks, and provides detailed feedback directly on the pull requests.

**Main Functions:**

*   **Automated PR Monitoring**: Periodically checks configured GitHub repositories for new or updated pull requests.
*   **Comprehensive Code Review**:
    *   **Typo and Grammar Check**: Identifies and suggests corrections for spelling and grammar errors in code, comments, and documentation, optionally leveraging an AI model for advanced analysis.
    *   **AI-Powered Code Quality Review**: Utilizes AI (OpenAI or Anthropic) to assess code for quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Detection**: Scans code for common security risks such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **Automated Feedback**: Posts detailed inline comments on specific lines of code where issues are found, along with a comprehensive summary comment on the pull request.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests that pass all configured checks without any detected issues.
*   **Configurable Behavior**: Allows customization of review types (typos, code quality, security), limits on file and line changes for review, polling frequency, and the agent's display name in comments.

**Inputs:**

*   **GitHub API (Polling)**: Fetches pull request details, file changes, and existing comments from monitored repositories.
*   **Environment Variables**: Configuration settings for GitHub authentication, AI service selection and API keys, review preferences, repository lists, and operational parameters.
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token.
    *   `AI_PROVIDER`: "openai" or "anthropic".
    *   `OPENAI_API_KEY`: Required if `AI_PROVIDER` is "openai".
    *   `ANTHROPIC_API_KEY`: Required if `AI_PROVIDER` is "anthropic".
    *   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`: Enable/disable typo review (`true`/`false`).
    *   `REVIEW_CODE_QUALITY`: Enable/disable AI code quality review (`true`/`false`).
    *   `REVIEW_SECURITY`: Enable/disable security review (`true`/`false`).
    *   `AUTO_APPROVE_MINOR`: Enable/disable auto-approval (`true`/`false`).
    *   `MAX_FILES_PER_REVIEW`: Maximum files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
    *   `AGENT_NAME`: Name used in PR comments (default: "PR Review Bot").
    *   `POLLING_INTERVAL`: Frequency (in seconds) to check for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **Command Line Arguments**: Used for manual triggering of a specific PR review or interactive setup of the agent.

**Outputs:**

*   **GitHub API**: Posts new comments (inline and summary) on pull requests.
*   **GitHub API**: Submits PR approvals if configured and no issues are found.
*   **Stdout/Logs**: Provides operational logs and status updates during execution.