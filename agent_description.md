### Name
PR Review Agent

### Description
The PR Review Agent is an AI-powered tool designed for automated code review and typo detection on GitHub pull requests. It monitors specified repositories for new pull requests, performs comprehensive reviews covering code quality, security vulnerabilities, and potential typos, and then posts its findings as comments or approves the pull request based on its configuration.

### Functions
*   **Automated Pull Request Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Quality Review**: Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for quality, adherence to best practices, performance issues, and potential bugs.
*   **Security Vulnerability Detection**: Scans code for common security risks, including hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction**: Reviews newly added lines of code and comments for spelling and grammar errors, providing suggested corrections.
*   **Comment and Approval Management**: Posts detailed inline comments on specific lines of code where issues are found, provides a summary comment for the entire pull request, and can automatically approve PRs if no issues are detected.
*   **Configurable Review Scope**: Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **On-Demand Review**: Can be manually triggered to review a specific pull request by its repository URL and number.

### Inputs
*   **GitHub API**: Pull request data (e.g., files, diffs, existing comments) from monitored or specified repositories.
*   **Environment Variables**: Configuration parameters loaded from the environment (or a `.env` file), including GitHub authentication tokens, AI provider API keys, a list of repositories to monitor, and various review settings.

### Outputs
*   **GitHub Comments (HTTP)**: Posts inline comments on specific lines of code and a comprehensive summary comment on the pull request.
*   **GitHub PR Status (HTTP)**: Can approve pull requests if configured to do so and no issues are found.
*   **Console/Log Output (stdout)**: Provides detailed logs about its operational status, review progress, and any errors encountered.

### Configuration
The agent is highly configurable via environment variables, which can be set directly or loaded from a `.env` file. Key configuration options include:
*   `GITHUB_TOKEN`: Your GitHub Personal Access Token for API authentication.
*   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
*   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
*   `WATCHED_REPOSITORIES`: A comma-separated list of `owner/repo` pairs to monitor.
*   `REVIEW_TYPOS`: Enables/disables typo and grammar review (`true`/`false`).
*   `REVIEW_CODE_QUALITY`: Enables/disables AI-powered code quality review (`true`/`false`).
*   `REVIEW_SECURITY`: Enables/disables security vulnerability review (`true`/`false`).
*   `AUTO_APPROVE_MINOR`: Automatically approves PRs with no issues (`true`/`false`).
*   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
*   `MAX_LINES_PER_FILE`: Maximum number of lines per file to review.
*   `AGENT_NAME`: The name the agent uses when posting comments (defaults to "PR Review Bot").
*   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.