### Agent Name
PR Review Agent

### Summary
The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews, including typo detection, AI-driven code quality analysis, and security vulnerability checks. The agent then posts detailed comments directly on the pull request, providing feedback and suggestions, and can optionally approve PRs with no issues found.

### Key Features
*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Review:**
    *   **Typo and Grammar Review:** Identifies and suggests corrections for spelling and grammar errors in code and documentation.
    *   **AI-Powered Code Quality Review:** Utilizes large language models (LLMs) to analyze code for best practices, readability, performance issues, and potential bugs.
    *   **Security Vulnerability Detection:** Scans for common security risks like hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
*   **GitHub Integration:** Posts review comments directly on pull requests, including inline suggestions for specific lines and a summary of findings.
*   **Configurable Behavior:** Allows customization of review types, AI provider (OpenAI or Anthropic), review scope (max files/lines), polling interval, and automatic approval for minor PRs.
*   **Dry Run Mode:** Supports a dry-run mode to preview review comments without posting them to GitHub.

### Inputs
*   **Environment Variables:**
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY`: API key for OpenAI (if `AI_PROVIDER` is `openai`).
    *   `ANTHROPIC_API_KEY`: API key for Anthropic (if `AI_PROVIDER` is `anthropic`).
    *   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`: Enables/disables typo review (`true`/`false`).
    *   `REVIEW_CODE_QUALITY`: Enables/disables AI code quality review (`true`/`false`).
    *   `REVIEW_SECURITY`: Enables/disables security review (`true`/`false`).
    *   `AUTO_APPROVE_MINOR`: Enables/disables auto-approval for PRs with no issues (`true`/`false`).
    *   `MAX_FILES_PER_REVIEW`: Maximum files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
    *   `AGENT_NAME`: The name used by the agent in PR comments (default: "PR Review Bot").
    *   `POLLING_INTERVAL`: Frequency (in seconds) to check for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **Command-Line Arguments (for specific PR review):**
    *   `repo_url`: The URL of the GitHub repository.
    *   `pr_number`: The pull request number.

### Outputs
*   **GitHub Comments:** Posts detailed review comments directly on the pull request, including inline suggestions and a summary of findings.
*   **GitHub Approvals:** Can approve pull requests if configured to do so and no issues are found.
*   **Stdout/Logs:** Provides operational logs and status updates to the console.