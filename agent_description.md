**Agent Name:** PR Review Agent

**Summary:**
The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It actively monitors specified repositories for new pull requests, performing comprehensive checks for code quality, potential security vulnerabilities, and grammatical/spelling errors. Based on its findings, the agent posts detailed comments directly on the pull request, providing actionable feedback, or approves the PR if no issues are detected.

**Main Functions:**
*   **Automated Pull Request Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Quality Review:** Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for best practices, performance issues, and potential bugs, providing detailed suggestions.
*   **Security Vulnerability Detection:** Scans code for common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors within the pull request's changed lines.
*   **Automated Feedback:** Posts inline comments on specific lines of code with identified issues and provides a comprehensive summary comment on the pull request.
*   **Conditional PR Approval:** Can be configured to automatically approve pull requests that pass all review checks without any detected issues.

**Key Features:**
*   **Configurable Review Scope:** Users can enable or disable specific review types (typos, code quality, security) to tailor the agent's behavior.
*   **AI Provider Flexibility:** Supports both OpenAI and Anthropic as AI backends for intelligent code analysis.
*   **Scalable Review Limits:** Configurable limits on the number of files and lines per file to review, managing performance and API usage.
*   **Dry Run Mode:** Allows testing the agent's review capabilities without actually posting comments to GitHub.
*   **Interactive Setup:** Provides a command-line utility for initial configuration setup.

**Inputs:**
*   **Environment Variables:** The agent is configured primarily through environment variables, which can be loaded from a `.env` file. These include:
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable automatic approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `AGENT_NAME`: The name used by the agent in its comments (defaults to "PR Review Bot").
    *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **Command Line Arguments:**
    *   `pr-review-agent start`: Initiates continuous monitoring with options for config file, dry run, and verbose logging.
    *   `pr-review-agent review <repo_url> <pr_number>`: Triggers a review for a specific pull request.

**Outputs:**
*   **GitHub Pull Request Comments:** (HTTP) The agent posts detailed inline comments on specific lines of code and a summary comment on the pull request itself.
*   **GitHub Pull Request Approvals:** (HTTP) If configured and no issues are found, the agent can approve the pull request.
*   **Console/Log Output:** (stdout) Provides status updates, errors, and debugging information during operation.