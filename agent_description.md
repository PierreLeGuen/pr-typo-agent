## PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It actively monitors specified repositories for new pull requests and performs comprehensive reviews, identifying potential issues related to code quality, security vulnerabilities, and typos. Based on its findings, the agent posts detailed comments or approves pull requests directly on GitHub.

### Key Features

*   **Automated Pull Request Monitoring:** Continuously checks designated GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review:** Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for quality, best practices, performance issues, and potential bugs.
*   **Typo and Grammar Detection:** Scans new code changes for spelling and grammatical errors, suggesting corrections.
*   **Security Vulnerability Analysis:** Identifies common security risks such as hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
*   **Configurable Review Scope:** Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per PR.
*   **Automated PR Approval:** Can be configured to automatically approve pull requests where no issues are detected.
*   **Detailed Feedback:** Posts inline comments directly on GitHub for specific findings and provides a summary comment for the overall review.
*   **Flexible Deployment:** Configurable via environment variables for easy setup and integration.
*   **On-Demand Review:** Supports reviewing specific pull requests manually via command-line.

### Inputs

*   **Environment Variables:**
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token with repository permissions.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., `openai` or `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable automatic approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `AGENT_NAME`: The name the bot uses in PR comments (defaults to "PR Review Bot").
    *   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.
    *   `GITHUB_WEBHOOK_SECRET`, `MAX_RETRIES`: Optional advanced configurations.
*   **Command Line (for specific PR review):**
    *   `repo_url` (e.g., `https://github.com/owner/repo`)
    *   `pr_number` (e.g., `123`)

### Outputs

*   **GitHub Comments:**
    *   Inline comments on specific lines of code detailing typos, code quality suggestions, or security findings.
    *   A summary comment on the pull request, listing the types and counts of issues found.
*   **GitHub PR Status:**
    *   Approval of the pull request if `AUTO_APPROVE_MINOR` is enabled and no issues are detected.
*   **Console Output:**
    *   Logs of agent activity, status updates, and errors.