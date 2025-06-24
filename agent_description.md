### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors designated repositories for new pull requests and provides comprehensive feedback on various aspects of the code, including quality, security, and typos.

**Key Features:**

*   **Automated Pull Request Review**: Continuously monitors specified GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Analysis**: Performs detailed reviews covering:
    *   **Code Quality**: Utilizes advanced AI models (OpenAI or Anthropic) to assess code quality, adherence to best practices, and potential performance issues.
    *   **Security Vulnerability Detection**: Identifies common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
    *   **Typo and Grammar Correction**: Checks for spelling and grammar errors in code, comments, and documentation, suggesting corrections.
*   **Configurable Review Scope**: Users can enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **Intelligent Feedback**: Posts detailed inline comments on specific lines of code where issues are found and provides a comprehensive summary comment on the pull request.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests that pass all configured checks without any issues.
*   **On-Demand Review**: Supports reviewing a specific pull request manually via a command-line interface.

**Inputs:**

*   **Medium**: GitHub API (for polling pull requests), Environment Variables, Command Line Interface.
*   **Details**:
    *   **GitHub Events**: Monitors new and updated pull requests in configured repositories.
    *   **Environment Variables**: Configuration parameters such as GitHub API token, AI provider API keys, list of watched repositories, and various review settings (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `OPENAI_API_KEY`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`, `AGENT_NAME`, `POLLING_INTERVAL`, `MAX_RETRIES`).
    *   **Command Line Arguments**: For triggering a review on a specific PR or starting the agent's continuous monitoring.

**Outputs:**

*   **Medium**: GitHub API (for posting comments and approvals), stdout (for logging).
*   **Details**:
    *   **GitHub Pull Request Comments**: Posts detailed comments on specific lines of code and a summary comment on the pull request, highlighting detected issues and suggestions.
    *   **GitHub Pull Request Approvals**: Optionally approves pull requests if no issues are found, based on configuration.
    *   **Console Logs**: Provides operational logs, status updates, and error messages to the standard output.