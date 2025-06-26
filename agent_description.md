### PR Review Agent

The PR Review Agent is an AI-powered assistant designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new or updated pull requests and performs comprehensive reviews covering code quality, potential security vulnerabilities, and grammatical/typographical errors.

#### Main Functions
*   **Automated Pull Request Monitoring**: Watches configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review**: Utilizes AI models (OpenAI or Anthropic) to analyze code changes for quality, best practices, and potential issues.
*   **Security Vulnerability Detection**: Identifies common security risks such as hardcoded secrets, SQL injection patterns, and weak cryptographic algorithms.
*   **Typo and Grammar Checking**: Reviews added lines of code for spelling and grammar mistakes, offering suggestions for correction.
*   **Automated Feedback**: Posts detailed inline comments on specific lines where issues are found and provides a comprehensive summary comment on the pull request.
*   **Conditional Approval**: Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Configurable Review Scope**: Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.

#### Inputs
*   **Environment Variables**: Configuration is primarily managed through environment variables, including GitHub API tokens, AI provider API keys, watched repositories, review preferences (e.g., `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`), and operational settings (e.g., `POLLING_INTERVAL`, `MAX_FILES_PER_REVIEW`).
*   **GitHub Pull Requests**: The agent processes pull request data fetched from GitHub via its API.
*   **Command Line (stdin)**: Can be invoked to review a specific pull request by providing the repository URL and PR number.

#### Outputs
*   **GitHub Comments**: The agent posts comments on pull requests, including inline suggestions for specific issues and a summary of its findings.
*   **GitHub Approvals**: If configured and no issues are found, the agent may post an approval on the pull request.
*   **Console/Log Output (stdout)**: Provides operational logs, status updates, and error messages.