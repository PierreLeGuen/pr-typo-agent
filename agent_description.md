### PR Review Agent

The PR Review Agent is an AI-powered agent designed for automated code review and typo detection on GitHub pull requests. It continuously monitors specified repositories or can review a specific PR on demand, providing feedback on code quality, security, and potential typos by posting comments directly on the pull request.

#### Key Functions

*   **Automated Pull Request Review**: Monitors configured GitHub repositories for new or updated pull requests, or reviews a specific PR when invoked.
*   **AI-Powered Code Analysis**: Utilizes AI models (OpenAI or Anthropic) to review code for quality, readability, performance issues, and best practices violations.
*   **Typo and Grammar Detection**: Identifies and suggests corrections for spelling and grammar errors in new or changed lines of code and documentation.
*   **Security Vulnerability Scanning**: Scans for common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **GitHub Integration**: Posts detailed inline comments for specific findings and a comprehensive summary comment on the pull request.
*   **Configurable Behavior**: Allows customization of review types (typos, code quality, security), maximum files/lines to review, polling interval, and optional automatic approval for clean PRs.

#### Inputs

*   **Medium**: HTTP (via GitHub API)
*   **Data**:
    *   GitHub Pull Request data (files, diffs, comments) retrieved from the GitHub API.
    *   Configuration settings provided through environment variables.

#### Outputs

*   **Medium**: HTTP (via GitHub API)
*   **Data**:
    *   GitHub Pull Request comments: Detailed inline comments with suggested changes and a summary report at the end of the review.
    *   GitHub Pull Request approvals: Optionally approves pull requests if no issues are detected during the review.

#### Environment Variables

The agent's behavior is configured via environment variables:

*   **`GITHUB_TOKEN`**: Your GitHub Personal Access Token with `repo` permissions.
*   **`AI_PROVIDER`**: The AI service provider to use ("openai" or "anthropic").
*   **`OPENAI_API_KEY`**: Your OpenAI API key (if `AI_PROVIDER` is "openai").
*   **`ANTHROPIC_API_KEY`**: Your Anthropic API key (if `AI_PROVIDER` is "anthropic").
*   **`WATCHED_REPOSITORIES`**: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
*   **`REVIEW_TYPOS`**: Set to `true` to enable typo and grammar review.
*   **`REVIEW_CODE_QUALITY`**: Set to `true` to enable AI-powered code quality review.
*   **`REVIEW_SECURITY`**: Set to `true` to enable security vulnerability review.
*   **`AUTO_APPROVE_MINOR`**: Set to `true` to automatically approve pull requests with no issues found.
*   **`MAX_FILES_PER_REVIEW`**: Maximum number of files to review per PR.
*   **`MAX_LINES_PER_FILE`**: Maximum lines to review per file.
*   **`AGENT_NAME`**: The name the agent uses in PR comments (default: "PR Review Bot").
*   **`POLLING_INTERVAL`**: How often (in seconds) to check for new PRs (default: 300).
*   **`MAX_RETRIES`**: Maximum retries for API calls.
*   **`GITHUB_WEBHOOK_SECRET`**: Optional secret for GitHub webhook validation.