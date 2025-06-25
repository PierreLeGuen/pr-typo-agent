### PR Review Agent

The PR Review Agent is an AI-powered automation tool designed to enhance code review processes on GitHub. It monitors specified repositories for new or updated pull requests and performs automated checks for various issues.

**Main Functions:**
*   **Automated Pull Request Review**: Continuously monitors designated GitHub repositories for open pull requests.
*   **Typo and Grammar Detection**: Reviews added code lines and comments for spelling and grammatical errors, suggesting corrections.
*   **AI-Powered Code Quality Analysis**: Utilizes advanced AI models (OpenAI or Anthropic) to identify potential code quality issues, best practice violations, and performance concerns in changed code.
*   **Security Vulnerability Scanning**: Detects common security risks such as hardcoded secrets, SQL injection vulnerabilities, and command injection patterns.
*   **Automated Feedback**: Posts detailed comments directly on the pull request, including inline suggestions for specific lines and a comprehensive summary of findings.
*   **Conditional Approval**: Can be configured to automatically approve pull requests where no issues are detected.

**Key Features:**
*   Configurable to enable or disable specific review types (typos, code quality, security).
*   Supports both OpenAI and Anthropic as AI service providers.
*   Allows setting limits on the number of files and lines reviewed per pull request to manage scope.
*   Can operate in a continuous polling mode or review a specific pull request on demand.

**Inputs:**
*   **GitHub API**: Accesses pull request data (files, diffs, comments) from configured repositories.
*   **Environment Variables**: Configuration parameters for GitHub authentication, AI API keys, review settings, watched repositories, and agent behavior.
*   **Command Line (for on-demand review)**: Repository URL and pull request number.

**Outputs:**
*   **GitHub API**: Posts comments (inline and summary) on pull requests and can submit approvals.
*   **Console/Logs**: Provides status updates, error messages, and detailed logging information.