## PR Review Agent

An AI-powered agent designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories, applying intelligent analysis to identify and report various issues directly within the PR.

### Key Features

*   **Automated Code Review:** Leverages AI (OpenAI or Anthropic) to review pull requests for code quality, adherence to best practices, and potential bugs.
*   **Security Vulnerability Detection:** Scans code for common security risks such as hardcoded secrets, SQL injection patterns, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammatical errors in code, comments, and documentation.
*   **Configurable Review Scope:** Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per PR.
*   **Flexible Operation:** Can operate in a continuous monitoring mode, polling GitHub for new pull requests, or be triggered to review a specific pull request on demand.
*   **GitHub Integration:** Posts detailed findings as inline comments on specific lines of code and provides a summary comment on the overall pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests where no issues are detected.

### Inputs

*   **Environment Variables:**
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: The AI service to use for reviews (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`: `true` or `false` to enable/disable typo review.
    *   `REVIEW_CODE_QUALITY`: `true` or `false` to enable/disable AI code quality review.
    *   `REVIEW_SECURITY`: `true` or `false` to enable/disable security review.
    *   `AUTO_APPROVE_MINOR`: `true` or `false` to enable/disable auto-approval for clean PRs.
    *   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum number of lines to review per file.
    *   `AGENT_NAME`: The name the agent uses in PR comments.
    *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: (Optional) Secret for webhook validation.
*   **Command-Line Arguments:**
    *   `pr-review-agent start`: Starts the agent in continuous monitoring mode.
        *   `--config-file`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Prevents posting actual comments.
        *   `--verbose`: Enables detailed logging.
    *   `pr-review-agent review <repo_url> <pr_number>`: Reviews a specific pull request.
        *   `repo_url`: The full URL of the repository (e.g., `https://github.com/owner/repo`).
        *   `pr_number`: The pull request number.
        *   `--config-file`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Prevents posting actual comments.
    *   `pr-review-agent setup`: Provides an interactive prompt to generate a basic `.env` configuration file.

### Outputs

*   **GitHub Comments:**
    *   Inline comments on specific lines of code highlighting issues (typos, code quality, security).
    *   A summary comment on the pull request, detailing findings or confirming no issues found.
*   **GitHub Pull Request Approvals:** (Conditional) Posts an approval comment if `AUTO_APPROVE_MINOR` is enabled and no issues are found.
*   **Console/Log Output:** Provides real-time status updates, warnings, and error messages during operation.