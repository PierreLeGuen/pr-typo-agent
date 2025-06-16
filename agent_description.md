## PR Review Agent

An AI-powered agent for automated code review and typo detection on GitHub pull requests. It monitors specified repositories for new pull requests, reviews code quality, security, and typos, and posts comments or approvals based on its findings.

### Key Features

*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Comprehensive Code Review**:
    *   **Typo and Grammar Check**: Identifies and suggests corrections for spelling and grammar errors in new code.
    *   **AI-Powered Code Quality**: Utilizes large language models (LLMs) from OpenAI or Anthropic to review code for quality, best practices, performance issues, and potential bugs.
    *   **Security Vulnerability Detection**: Scans for common security issues like hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
*   **Detailed Feedback**: Posts inline comments on specific lines of code where issues are found, along with a summary comment on the pull request.
*   **Configurable Behavior**: Allows customization of review types, file/line limits, polling intervals, and automatic approval for clean PRs.
*   **Specific PR Review**: Can be invoked to review a single, specified pull request on demand.

### Inputs

*   **Environment Variables**: Configuration parameters loaded from the environment, including GitHub token, AI provider API keys, watched repositories, review preferences, and operational settings.
*   **GitHub API (HTTP)**: Pull request data, file changes (patches), and existing comments are fetched from GitHub.
*   **Command Line Arguments (stdin)**: For the `review` command, takes a repository URL and pull request number.

### Outputs

*   **GitHub API (HTTP)**: Posts new comments on pull requests (inline review comments, general summary comments, or approval messages).
*   **Console/Logs (stdout/stderr)**: Provides operational logs, status updates, and error messages.

### Configuration

The agent is configured primarily through environment variables, allowing users to specify:
*   GitHub authentication (`GITHUB_TOKEN`, `GITHUB_WEBHOOK_SECRET`).
*   AI provider and API keys (`AI_PROVIDER`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).
*   Enabled review types (`REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`).
*   Review behavior (`AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`).
*   Repositories to monitor (`WATCHED_REPOSITORIES`).
*   Agent identity and operational timing (`AGENT_NAME`, `POLLING_INTERVAL`, `MAX_RETRIES`).