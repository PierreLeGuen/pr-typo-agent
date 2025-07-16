### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process for GitHub pull requests. It monitors specified repositories, analyzes new pull requests for various issues, and provides feedback directly on GitHub.

**Main Functions:**
*   **Automated Pull Request Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review**: Utilizes an AI model (OpenAI or Anthropic) to assess code quality, identify potential bugs, and suggest best practices.
*   **Typo and Grammar Detection**: Reviews new and changed lines of code and documentation for spelling and grammar errors, offering suggestions for correction.
*   **Security Vulnerability Scanning**: Scans code for common security issues such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **Intelligent Commenting**: Posts detailed review comments directly on GitHub pull requests, highlighting specific issues and suggesting improvements.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests that pass all configured reviews without any issues found.
*   **Configurable Review Scope**: Allows setting limits on the maximum number of files and lines per file to review, and enables/disables specific review types (typos, code quality, security).
*   **On-Demand Review**: Can be triggered to review a specific pull request by its repository URL and PR number.

**Inputs:**
*   **Environment Variables**: Configured via environment variables (e.g., loaded from a `.env` file) for GitHub authentication, AI service selection and API keys, monitored repositories, review settings (e.g., `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`), and operational parameters (e.g., `POLLING_INTERVAL`, `AGENT_NAME`).
*   **Command-line Arguments**: For specific tasks like reviewing a single PR (`repo_url`, `pr_number`) or running in dry-run mode.

**Outputs:**
*   **GitHub Pull Request Comments**: Posts inline comments on specific lines of code and a summary comment for the entire pull request via the GitHub API.
*   **GitHub Pull Request Approvals**: Submits an approval status for pull requests that meet the auto-approval criteria via the GitHub API.
*   **Console Logs**: Provides operational logs and status updates to standard output.