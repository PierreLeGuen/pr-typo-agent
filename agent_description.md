### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests, applies various review checks, and provides detailed feedback directly on GitHub.

**Key Features:**

*   **Automated PR Review**: Monitors configured GitHub repositories for new pull requests, initiating reviews automatically.
*   **Multi-faceted Review**: Conducts comprehensive checks, including:
    *   **Typo and Grammar Detection**: Identifies spelling and grammatical errors in new or modified code lines.
    *   **AI-Powered Code Quality**: Utilizes large language models (OpenAI or Anthropic) to assess code quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Scanning**: Detects common security issues such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **Actionable Feedback**: Posts detailed inline comments on specific lines of code where issues are found, along with suggested improvements. It also provides a comprehensive summary comment on the pull request.
*   **Conditional Approval**: Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Configurable Scope**: Allows users to define limits on the maximum number of files and lines per file to be reviewed, preventing excessively large PRs from being fully processed.
*   **Flexible Operation**: Can run in a continuous polling mode to monitor repositories or be invoked on demand to review a specific pull request.

**Inputs:**

*   **GitHub API**: Fetches pull request details, changed files, and existing comments.
*   **Environment Variables**: Configuration settings loaded from the environment or a `.env` file.

**Outputs:**

*   **GitHub Comments**: Posts inline review comments and a summary comment on pull requests.
*   **GitHub Approvals**: Optionally approves pull requests if no issues are found.
*   **Console/Logs**: Provides operational logs and status updates.

**Configuration:**

The agent is highly configurable via environment variables, allowing users to:

*   Specify GitHub authentication (`GITHUB_TOKEN`).
*   Choose the AI provider (`AI_PROVIDER`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).
*   Enable/disable specific review types (`REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`).
*   Configure review behavior (`AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`).
*   Define repositories to monitor (`WATCHED_REPOSITORIES`).
*   Set agent identity and operational parameters (`AGENT_NAME`, `POLLING_INTERVAL`, `MAX_RETRIES`).