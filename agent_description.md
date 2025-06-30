### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It actively monitors specified repositories for new pull requests, applies various checks, and provides detailed feedback directly on GitHub.

**Main Functions:**

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Comprehensive Code Review:** Performs multi-faceted analysis of pull request changes, including:
    *   **Typo and Grammar Review:** Identifies and suggests corrections for spelling and grammatical errors in code and comments.
    *   **AI-Powered Code Quality Review:** Leverages AI models (OpenAI or Anthropic) to assess code quality, readability, adherence to best practices, and potential bugs.
    *   **Security Vulnerability Detection:** Scans for common security issues like hardcoded secrets, potential SQL injection, and command injection vulnerabilities.
*   **Intelligent Feedback:** Posts review comments directly on GitHub, either as inline suggestions on specific lines of code or as a summary comment for the entire pull request.
*   **Conditional Approval:** Can be configured to automatically approve pull requests if no issues are found during the review.
*   **On-Demand Review:** Allows users to trigger a review for a specific pull request manually.
*   **Configurable Behavior:** Users can enable or disable specific review types (typos, code quality, security), set limits on files and lines reviewed, and choose their preferred AI provider.

**Inputs:**

*   **Configuration:** Environment variables or a `.env` file specifying GitHub tokens, AI API keys, watched repositories, and review preferences.
*   **GitHub Pull Request Data:** Fetches pull request details, file changes (diffs), and existing comments via the GitHub API.
*   **Command-Line Arguments:** For initiating on-demand reviews of specific pull requests (e.g., repository URL, PR number).

**Outputs:**

*   **GitHub Pull Request Comments:** Posts detailed review findings, suggestions, and summary comments directly to the pull request on GitHub.
*   **Console Output:** Provides status updates and logging information to the standard output.

**Configuration:**

The agent's behavior is highly configurable through environment variables, allowing users to customize:

*   **`GITHUB_TOKEN`**: Your GitHub Personal Access Token for API authentication.
*   **`AI_PROVIDER`**: Choice of AI service (e.g., `openai`, `anthropic`).
*   **`OPENAI_API_KEY` / `ANTHROPIC_API_KEY`**: API keys for the chosen AI provider.
*   **`WATCHED_REPOSITORIES`**: A comma-separated list of GitHub repositories to monitor.
*   **`REVIEW_TYPOS`**: Enable/disable typo and grammar checks.
*   **`REVIEW_CODE_QUALITY`**: Enable/disable AI-powered code quality review.
*   **`REVIEW_SECURITY`**: Enable/disable security vulnerability review.
*   **`AUTO_APPROVE_MINOR`**: Enable/disable automatic approval for clean PRs.
*   **`MAX_FILES_PER_REVIEW`**: Limits the number of files reviewed per PR.
*   **`MAX_LINES_PER_FILE`**: Limits the lines reviewed per file.
*   **`POLLING_INTERVAL`**: How often the agent checks for new PRs.
*   **`AGENT_NAME`**: The name displayed in PR comments.