### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It monitors specified repositories for new or updated pull requests and performs comprehensive checks for code quality, security vulnerabilities, and grammatical errors. Based on its findings, the agent posts detailed feedback or approvals directly on the pull request.

#### Main Functions

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Quality Review:** Utilizes large language models (LLMs) from providers like OpenAI or Anthropic to analyze code changes for best practices, potential bugs, and readability issues.
*   **Security Vulnerability Detection:** Scans code for common security concerns, including hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction:** Reviews added lines of code and comments for spelling and grammatical errors, suggesting corrections.
*   **Automated Feedback and Approval:** Posts detailed inline comments for specific issues found and provides a summary comment on the pull request. It can also be configured to automatically approve pull requests that pass all checks without issues.
*   **Interactive Setup:** Offers a command-line utility to guide users through the initial configuration of essential settings.

#### Key Features

*   Supports integration with OpenAI and Anthropic API services for AI-driven reviews.
*   Allows users to enable or disable specific review types (typos, code quality, security) based on their needs.
*   Configurable limits on the number of files and lines reviewed per pull request to manage scope.
*   Option to automatically approve pull requests if no issues are detected.
*   Customizable polling interval for checking new pull requests.
*   Authenticates with GitHub using a Personal Access Token for secure operations.

#### Inputs

*   **Environment Variables:** Configured via environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `MAX_FILES_PER_REVIEW`, `AGENT_NAME`, `POLLING_INTERVAL`). These are typically loaded from a `.env` file.
*   **GitHub Pull Request Data (HTTP):** Reads code changes, file lists, and existing comments from monitored GitHub repositories via the GitHub API.
*   **Command Line Arguments (stdin):** For reviewing a specific PR, accepts `repo_url` and `pr_number` as arguments.

#### Outputs

*   **GitHub Pull Request Comments (HTTP):** Posts detailed inline comments on specific lines of code for identified issues (typos, code quality, security).
*   **GitHub Pull Request Summary (HTTP):** Adds a comprehensive summary comment to the pull request, outlining the review findings.
*   **GitHub Pull Request Approval (HTTP):** Can post an approval comment if no issues are found and the auto-approval feature is enabled.
*   **Console/Log Output (stdout/stderr):** Provides status updates, progress information, and error messages during operation.