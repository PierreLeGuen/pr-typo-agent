### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new or updated pull requests and performs comprehensive reviews based on configurable criteria.

**Main Functions:**

*   **Automated Pull Request Monitoring:** Watches a list of configured GitHub repositories for new pull requests.
*   **AI-Powered Code Review:** Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for quality, adherence to best practices, and potential bugs.
*   **Security Vulnerability Detection:** Scans code for common security issues such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors in new or modified code lines, optionally leveraging AI for improved accuracy.
*   **Automated Feedback:** Posts detailed review comments directly on GitHub pull requests, including inline suggestions and a summary of findings.
*   **Conditional Approval:** Can be configured to automatically approve pull requests if no issues are detected during the review.

**Key Features:**

*   **Configurable Review Types:** Users can enable or disable typo, code quality, and security reviews independently.
*   **Customizable Review Scope:** Limits the maximum number of files and lines reviewed per pull request to manage scope and resource usage.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic as AI providers for intelligent code analysis.
*   **Polling Mechanism:** Periodically checks for new pull requests based on a defined interval.
*   **On-Demand Review:** Allows users to trigger a review for a specific pull request manually via a command.

---

**Inputs:**

*   **GitHub Pull Requests:** Monitors new and updated pull requests from configured GitHub repositories.
*   **Environment Variables (via `.env` file or system):**
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Choice of AI service ("openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag for auto-approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits on review scope.
    *   `AGENT_NAME`: Name used in PR comments.
    *   `POLLING_INTERVAL`: Frequency of PR checks in seconds.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **Command Line Arguments:**
    *   `start`: Initiates continuous monitoring.
    *   `review <repo_url> <pr_number>`: Triggers a review for a specific PR.
    *   `setup`: Interactive configuration assistant.

---

**Outputs:**

*   **GitHub Pull Request Comments:** Posts detailed review comments, including inline suggestions and a summary of findings, or an approval message.
*   **Console/Log Output:** Provides operational status, errors, and debugging information.