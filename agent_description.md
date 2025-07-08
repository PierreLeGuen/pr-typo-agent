### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the pull request review process on GitHub. It monitors specified repositories for new or updated pull requests and performs comprehensive reviews, providing feedback directly on GitHub.

**Main Functions:**

*   **Automated PR Monitoring:** Continuously checks designated GitHub repositories for new or updated pull requests.
*   **Intelligent Code Review:** Utilizes AI models (OpenAI or Anthropic) to analyze code for quality, best practices, and potential issues.
*   **Typo and Grammar Detection:** Scans new code additions for spelling and grammar errors, suggesting corrections.
*   **Security Vulnerability Checks:** Identifies common security concerns and patterns within the code.
*   **Detailed Feedback:** Posts inline comments on specific lines of code and a summary comment on the pull request, detailing any findings.
*   **Conditional Approval:** Can be configured to automatically approve pull requests if no issues are detected.
*   **Configurable Reviews:** Allows users to enable or disable specific review types (typos, code quality, security) based on their needs.
*   **On-Demand Review:** Supports reviewing a specific pull request by providing its repository URL and PR number.

**Inputs:**

*   **Environment Variables:** Configuration settings such as GitHub API token, AI provider API keys, list of repositories to monitor, review preferences (e.g., enable/disable typo checks, code quality, security), maximum files/lines to review, agent name, and polling interval.
*   **GitHub API (Polling):** Automatically fetches pull request details and file changes from monitored repositories.
*   **Command Line Arguments:** For reviewing a specific PR, the repository URL and pull request number are provided as arguments.

**Outputs:**

*   **GitHub Pull Request Comments:** Posts detailed comments on specific lines of code and a summary comment on the pull request itself, outlining detected issues and suggestions.
*   **GitHub Pull Request Approvals:** If configured and no issues are found, the agent can approve the pull request.
*   **Console/Log Output:** Provides real-time status updates and logging information on its operations.