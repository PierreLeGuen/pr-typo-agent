### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and performs comprehensive automated reviews, providing feedback directly on GitHub.

**Main Functions:**

*   **Automated Pull Request Review:** Monitors configured GitHub repositories and automatically reviews new pull requests.
*   **Code Quality Analysis:** Utilizes AI models (OpenAI or Anthropic) to analyze code for quality, best practices, performance issues, and potential bugs.
*   **Typo and Grammar Detection:** Checks newly added lines in pull requests for spelling and grammar errors, suggesting corrections.
*   **Security Vulnerability Scanning:** Identifies potential security risks such as hardcoded secrets, SQL injection vulnerabilities, and command injection patterns.
*   **GitHub Integration:** Posts detailed review comments directly on pull request lines or as a summary comment.
*   **Conditional Approval:** Can be configured to automatically approve pull requests if no issues are detected.
*   **Flexible Operation:** Can run continuously, polling for new PRs, or be triggered to review a specific pull request on demand.

**Key Features:**

*   Configurable AI provider (OpenAI or Anthropic).
*   Toggleable review types (typos, code quality, security).
*   Limits on file and line changes reviewed per pull request to manage scope.
*   Dry-run mode for testing without posting comments.
*   Customizable agent name for comments.

**Inputs:**

*   **Environment Variables:**
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable automatic PR approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits on the scope of review.
    *   `AGENT_NAME`: The name used for comments posted by the agent.
    *   `POLLING_INTERVAL`: How frequently (in seconds) the agent checks for new PRs.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
    *   `MAX_RETRIES`: Maximum retries for API calls.
*   **Command-line Arguments:**
    *   `start`: Initiates continuous monitoring.
        *   `--config-file <path>`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Enables dry-run mode.
        *   `--verbose`: Enables verbose logging.
    *   `review`: Reviews a specific pull request.
        *   `<repo_url>`: Full URL of the repository.
        *   `<pr_number>`: The pull request number.
        *   `--config-file <path>`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Enables dry-run mode.
    *   `setup`: Interactive configuration setup.

**Outputs:**

*   **GitHub Pull Request Comments:**
    *   Inline comments on specific lines with findings (typos, code quality, security issues).
    *   Summary comments on the pull request detailing all issues found.
*   **GitHub Pull Request Approvals:**
    *   Posts an approval comment if `AUTO_APPROVE_MINOR` is enabled and no issues are found.
*   **Console/Log Output (stdout):**
    *   Status messages, progress updates, and error logs during operation.