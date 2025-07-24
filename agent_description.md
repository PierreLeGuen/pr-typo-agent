### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests, applies AI-driven analysis for code quality, detects typos, and identifies potential security vulnerabilities. Based on its findings, the agent posts detailed comments directly on the pull request or, if configured, automatically approves clean PRs.

#### Key Features

*   **Automated PR Monitoring:** Regularly checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review:** Utilizes OpenAI or Anthropic models to assess code quality, best practices, and potential bugs.
*   **Typo and Grammar Detection:** Scans new code and comments for spelling and grammatical errors, offering suggestions.
*   **Security Vulnerability Scanning:** Identifies common security risks such as hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
*   **Detailed Feedback:** Posts inline comments on specific lines of code and a comprehensive summary comment on the pull request.
*   **Conditional Approval:** Can be configured to automatically approve pull requests that pass all configured checks without issues.
*   **Configurable Review Scope:** Allows setting limits on the number of files and lines reviewed per pull request.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic API services.
*   **On-Demand Review:** Can be triggered to review a specific pull request manually.

#### Configuration

The agent's behavior is configured primarily through environment variables, which can be loaded from a `.env` file. Key configurations include:

*   **`GITHUB_TOKEN`**: A GitHub Personal Access Token with `repo` permissions, used for authenticating with the GitHub API.
*   **`AI_PROVIDER`**: Specifies the AI service provider to use for code quality and typo reviews. Choose "openai" or "anthropic".
*   **`OPENAI_API_KEY`**: The OpenAI API key. Required if `AI_PROVIDER` is set to "openai".
*   **`ANTHROPIC_API_KEY`**: The Anthropic API key. Required if `AI_PROVIDER` is set to "anthropic".
*   **`WATCHED_REPOSITORIES`**: A comma-separated list of GitHub repositories (e.g., 'owner/repo,owner/repo2') that the agent should monitor.
*   **`REVIEW_TYPOS`**: Enable or disable typo and grammar review.
*   **`REVIEW_CODE_QUALITY`**: Enable or disable AI-powered code quality review.
*   **`REVIEW_SECURITY`**: Enable or disable security vulnerability review.
*   **`AUTO_APPROVE_MINOR`**: Automatically approve pull requests where no issues are found.
*   **`MAX_FILES_PER_REVIEW`**: The maximum number of files the agent will review per pull request.
*   **`MAX_LINES_PER_FILE`**: The maximum number of lines per file that the agent will review.
*   **`AGENT_NAME`**: The name the agent uses when posting comments on pull requests (e.g., "PR Review Bot").
*   **`POLLING_INTERVAL`**: How often (in seconds) the agent should check for new pull requests.

#### Inputs

*   **GitHub API (HTTP):** Pull request data (diffs, files, comments, metadata) from monitored repositories.
*   **Command Line Arguments (stdin):** For manual review, takes repository URL and PR number.
*   **Environment Variables:** Configuration settings loaded at startup.

#### Outputs

*   **GitHub Comments (HTTP):** Posts review comments (inline and summary) on pull requests.
*   **GitHub PR Status (HTTP):** Can approve pull requests if configured.
*   **Console/Logs (stdout/stderr):** Provides operational logs, status updates, and error messages.