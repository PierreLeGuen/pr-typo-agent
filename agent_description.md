### PR Review Agent

The PR Review Agent is an AI-powered bot designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests, performs comprehensive reviews, and provides feedback directly on GitHub.

**Main Functions:**
*   **Automated Code Review:** Analyzes pull request code for various issues.
*   **Typo and Grammar Detection:** Identifies and suggests corrections for spelling and grammar errors in code comments, documentation, and strings.
*   **Code Quality Analysis:** Utilizes an AI model (OpenAI or Anthropic) to assess code quality, readability, performance, and best practices.
*   **Security Vulnerability Scanning:** Detects potential security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **GitHub Integration:** Posts detailed review comments, including inline suggestions, and provides a summary of findings directly on the pull request.
*   **Configurable Behavior:** Allows users to enable/disable specific review types, set limits on file and line review counts, and configure auto-approval for clean PRs.
*   **Flexible Operation:** Can run in a continuous polling mode to monitor multiple repositories or review a specific pull request on demand.

**Inputs:**
*   **Environment Variables:**
    *   `GITHUB_TOKEN`: A GitHub Personal Access Token with `repo` permissions for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable or disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to automatically approve PRs with no issues.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits the scope of review.
    *   `AGENT_NAME`: The name used for comments posted by the agent.
    *   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.
    *   `GITHUB_WEBHOOK_SECRET`: (Optional) Secret for webhook validation.
    *   `MAX_RETRIES`: Maximum retries for API calls.
*   **Command Line (for on-demand review):**
    *   `repo_url`: The URL of the GitHub repository.
    *   `pr_number`: The specific pull request number to review.

**Outputs:**
*   **GitHub Comments:** Posts inline comments on specific lines of code with detailed findings and suggestions.
*   **GitHub Pull Request Summary:** Provides a summary comment on the pull request outlining the types and counts of issues found.
*   **GitHub Pull Request Approval:** If configured and no issues are found, the agent can automatically approve the pull request.
*   **Console/Stdout:** Logs operational status, errors, and dry-run output.