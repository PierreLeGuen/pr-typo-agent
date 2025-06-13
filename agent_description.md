### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests, or can be triggered to review a specific PR, and provides comprehensive feedback on code quality, potential security vulnerabilities, and typographical errors.

**Key Features:**

*   **Automated PR Monitoring:** Watches designated GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review:** Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for quality, best practices, performance issues, and potential bugs.
*   **Security Vulnerability Detection:** Identifies common security risks such as hardcoded secrets, SQL injection patterns, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Checking:** Reviews code comments, documentation, and string literals for spelling and grammar mistakes, offering suggestions for correction.
*   **Detailed Feedback:** Posts inline comments on specific lines of code and a summary comment on the pull request, categorizing findings by type (typo, code quality, security).
*   **Configurable Review Types:** Allows users to enable or disable specific review categories (typos, code quality, security).
*   **Automatic Approval:** Can be configured to automatically approve pull requests if no issues are detected.
*   **Flexible Deployment:** Supports continuous operation (polling) or on-demand review of individual pull requests.

**Inputs:**

*   **Environment Variables:** Configuration settings such as GitHub API token, AI provider keys, watched repositories, review preferences (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `OPENAI_API_KEY`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`).
*   **Command Line Arguments (for specific PR review):** Repository URL and Pull Request number.

**Outputs:**

*   **GitHub Pull Request Comments:** Posts detailed inline comments on specific code lines and a summary comment on the pull request itself, indicating findings and suggestions.
*   **GitHub Pull Request Approvals:** May approve pull requests if configured and no issues are found.
*   **Console/Log Output:** Provides operational status, progress, and error messages during execution (stdout).