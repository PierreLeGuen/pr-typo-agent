### Agent Name
PR Review Agent

### Summary
The PR Review Agent is an AI-powered bot designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new pull requests, performs comprehensive reviews for code quality, security vulnerabilities, and typos, and then posts detailed comments or approvals directly on the pull requests.

### Key Features
*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review**: Utilizes OpenAI or Anthropic models to analyze code for quality, best practices, performance issues, and potential bugs.
*   **Security Analysis**: Identifies common security vulnerabilities such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Checking**: Reviews new code and comments for spelling and grammar errors, providing suggestions for correction.
*   **Configurable Review Types**: Allows users to enable or disable specific review categories (typos, code quality, security).
*   **Intelligent Commenting**: Posts inline comments for specific findings and a summary comment for the entire pull request.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Scalable Review Limits**: Configurable limits for the maximum number of files and lines reviewed per pull request to manage scope.
*   **On-Demand Review**: Supports reviewing a specific pull request by providing its repository URL and PR number.

### Inputs
*   **Environment Variables**: Configured via environment variables (e.g., from a `.env` file) for GitHub authentication, AI provider selection, watched repositories, review preferences, and operational parameters.
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Choice of AI service ("openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable/disable automatic approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `AGENT_NAME`: The name used by the bot in PR comments.
    *   `POLLING_INTERVAL`: Frequency (in seconds) for checking new PRs.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **Command Line Arguments (for on-demand review)**:
    *   `repo_url` (string): The URL of the GitHub repository.
    *   `pr_number` (integer): The pull request number.

### Outputs
*   **GitHub Pull Request Comments**:
    *   Inline comments on specific lines of code detailing issues (typos, code quality, security).
    *   A summary comment on the pull request providing an overview of findings.
*   **GitHub Pull Request Approvals**:
    *   Posts an approval comment if `AUTO_APPROVE_MINOR` is enabled and no issues are found.
*   **Console/Log Output**: Provides operational logs, status updates, and error messages.