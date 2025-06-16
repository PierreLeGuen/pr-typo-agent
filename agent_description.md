### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests, performs comprehensive reviews covering code quality, security, and typos, and then posts detailed feedback or approvals directly on the pull requests.

### Key Features

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Review:**
    *   **Typo and Grammar Check:** Identifies and suggests corrections for spelling and grammar errors in code and documentation, optionally leveraging AI.
    *   **AI-Powered Code Quality Review:** Analyzes code for quality, best practices, performance issues, and potential bugs using advanced AI models (OpenAI or Anthropic).
    *   **Security Vulnerability Detection:** Scans for common security risks like hardcoded secrets, SQL injection, command injection, and weak cryptography.
*   **GitHub Integration:** Posts inline comments on specific lines of code and provides a summary comment on the pull request.
*   **Configurable Behavior:** Allows users to enable/disable specific review types, set limits on file/line review size, and optionally auto-approve clean PRs.
*   **Flexible Operation:** Can operate in a continuous monitoring mode or review a specific pull request on demand.

### Configuration

The agent is configured primarily through environment variables, which can be loaded from a `.env` file. Key configurations include:

*   **GitHub Authentication:** `GITHUB_TOKEN` (required) for API access.
*   **AI Provider:** `AI_PROVIDER` (e.g., "openai", "anthropic") and corresponding API keys (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`).
*   **Repositories to Watch:** `WATCHED_REPOSITORIES` (comma-separated list of `owner/repo`).
*   **Review Type Toggles:** `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY` (true/false).
*   **Behavioral Settings:** `AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`, `POLLING_INTERVAL`.
*   **Agent Identity:** `AGENT_NAME` for comments posted on GitHub.

### Inputs

*   **GitHub API (HTTP):** Pull request data (diffs, files, comments, metadata) from monitored repositories.
*   **Environment Variables:** Configuration settings loaded at startup.
*   **Command Line Arguments (stdin):** For `review` command (repository URL, PR number) and `start` command (config file, dry-run, verbose flags).

### Outputs

*   **GitHub API (HTTP):**
    *   Inline review comments on specific lines of code within a pull request.
    *   Summary comments on the pull request.
    *   Pull request approvals (if `AUTO_APPROVE_MINOR` is enabled and no issues are found).
*   **Console/Logs (stdout/stderr):** Operational logs, status updates, and error messages.