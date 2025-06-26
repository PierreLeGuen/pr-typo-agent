### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews covering code quality, potential security vulnerabilities, and typographical errors. Based on its findings, the agent posts detailed comments directly on the pull request or automatically approves PRs that meet predefined criteria.

#### Key Features

*   **Automated Pull Request Monitoring:** Periodically checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review:** Utilizes advanced AI models (OpenAI or Anthropic) to assess code quality, identify best practice violations, performance issues, and potential bugs.
*   **Security Vulnerability Detection:** Scans code for common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors in new or modified code lines and comments.
*   **Configurable Review Scope:** Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per PR.
*   **Automated Approval:** Can be configured to automatically approve pull requests where no issues are detected.
*   **Detailed Feedback:** Posts inline comments for specific issues and a summary comment for the entire pull request, providing clear, actionable feedback.
*   **Dry Run Mode:** Supports a dry run mode to simulate reviews without posting actual comments, useful for testing configurations.

#### Inputs

*   **Environment Variables (via `.env` file or system environment):**
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag for auto-approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `AGENT_NAME`: The name used by the bot in comments.
    *   `POLLING_INTERVAL`: Frequency (in seconds) for checking new PRs.
*   **Command Line Arguments:**
    *   `start`: Initiates continuous monitoring.
        *   `--config-file`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Enables dry run mode.
        *   `--verbose`: Enables verbose logging.
    *   `review`: Reviews a specific pull request.
        *   `<repo_url>`: URL of the repository.
        *   `<pr_number>`: Number of the pull request.
        *   `--config-file`: Path to the configuration file.
        *   `--dry-run`: Enables dry run mode.
    *   `setup`: Interactive wizard to generate a basic `.env` configuration file.

#### Outputs

*   **GitHub Pull Request Comments:**
    *   Inline comments on specific lines of code where issues (typos, code quality, security) are found.
    *   Summary comments on the pull request detailing all findings.
    *   Approval comments if no issues are detected and auto-approval is enabled.
*   **Console/Log Output:**
    *   Status messages and logs indicating agent activity, PRs being reviewed, and any errors encountered.