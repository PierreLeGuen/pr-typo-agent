### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new pull requests and performs comprehensive reviews, identifying potential issues related to code quality, security vulnerabilities, and typos.

#### Key Features

*   **Automated PR Monitoring:** Continuously checks designated GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Review:**
    *   **Code Quality:** Utilizes AI models (OpenAI or Anthropic) to analyze code for best practices, readability, performance issues, and potential bugs.
    *   **Security Scanning:** Detects common security vulnerabilities such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
    *   **Typo and Grammar Check:** Reviews code and documentation for spelling and grammar errors, offering suggestions for correction.
*   **Intelligent Commenting:** Posts detailed inline comments on specific lines of code where issues are found, along with a summary comment on the pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Configurable Review Scope:** Allows users to enable/disable specific review types (typos, code quality, security) and set limits on the number of files and lines to review per pull request.
*   **On-Demand Review:** Supports reviewing a specific pull request by its repository URL and number.

#### Inputs

*   **Environment Variables:** Configured via environment variables (e.g., from a `.env` file) to provide GitHub authentication tokens, AI API keys, watched repositories, and various review settings.
*   **GitHub Pull Request Data (HTTP):** Reads pull request details, file changes (diffs), and existing comments directly from the GitHub API.
*   **Command Line Arguments (stdin):** Accepts arguments for specific tasks like reviewing a single PR (`repo_url`, `pr_number`) or setting up configuration.

#### Outputs

*   **GitHub Comments (HTTP):** Posts inline comments on specific lines of code and summary comments on the pull request.
*   **GitHub Approvals (HTTP):** Can optionally submit a pull request approval if no issues are found and auto-approval is enabled.
*   **Console Logs (stdout):** Provides real-time status updates and logging information about the agent's operations.