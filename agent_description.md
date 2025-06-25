**Name**: PR Review Agent

**Description**:
The PR Review Agent is an AI-powered automation tool designed to enhance code review processes on GitHub. It continuously monitors designated repositories for new pull requests and performs comprehensive automated reviews. The agent checks for various aspects including typos, code quality, and potential security vulnerabilities. Based on its findings, it posts detailed comments directly on the pull request, providing actionable feedback or automatically approving PRs that meet the configured quality standards.

**Functions**:
*   **Automated Pull Request Monitoring**: Periodically checks specified GitHub repositories for newly opened or updated pull requests.
*   **Intelligent Code Review**: Utilizes AI (configurable with OpenAI or Anthropic) to analyze code changes for:
    *   **Typo and Grammar Corrections**: Identifies and suggests fixes for spelling and grammatical errors in code and comments.
    *   **Code Quality Assessment**: Provides feedback on code structure, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Detection**: Scans for common security issues like hardcoded secrets, SQL injection risks, and weak cryptographic algorithms.
*   **Feedback and Collaboration**: Posts clear and concise comments directly on the pull request, including inline suggestions for specific lines of code.
*   **Automated Approval**: Can be configured to automatically approve pull requests that pass all configured review checks without any identified issues.

**Inputs**:
*   **Environment Variables**: Configuration is provided via environment variables (typically loaded from a `.env` file), including GitHub authentication tokens, AI provider API keys, watched repositories, and various review settings (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `OPENAI_API_KEY`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AUTO_APPROVE_MINOR`, `POLLING_INTERVAL`).
*   **GitHub API**: Receives pull request data, file changes, and existing comments from the GitHub API.
*   **Command Line (for specific PR review)**: Repository URL and Pull Request number.

**Outputs**:
*   **GitHub API**: Posts new comments (inline and summary) on pull requests and can submit pull request approvals.
*   **Stdout**: Provides operational logs and status updates.