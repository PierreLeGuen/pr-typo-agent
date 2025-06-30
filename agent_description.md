### PR Review Agent

The PR Review Agent is an AI-powered automation tool designed to enhance code review processes on GitHub. It monitors specified repositories for new pull requests and performs automated reviews covering code quality, security vulnerabilities, and typographical errors.

**Main Functions:**

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Comprehensive Code Review:**
    *   **Typo and Grammar Check:** Identifies and suggests corrections for spelling and grammar mistakes in new code.
    *   **AI-Powered Code Quality Review:** Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for best practices, potential bugs, and performance issues.
    *   **Security Vulnerability Detection:** Scans for common security risks such as hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
*   **Automated Feedback:** Posts detailed review comments directly on GitHub pull requests, including inline suggestions for specific lines of code and a comprehensive summary of findings.
*   **Conditional Approval:** Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **On-Demand Review:** Supports reviewing specific pull requests by providing the repository URL and PR number.

**Key Features:**

*   Configurable to enable or disable specific review types (typos, code quality, security).
*   Supports integration with OpenAI or Anthropic AI services for intelligent analysis.
*   Limits the number of files and lines reviewed per pull request to manage scope and resource usage.
*   Operates with a configurable polling interval to check for new PRs.
*   Includes a dry-run mode for testing without posting actual comments.

**Inputs:**

*   **GitHub API:** Fetches pull request details, file changes, and existing comments.
*   **Environment Variables:** Configuration settings including GitHub authentication tokens, AI API keys, watched repositories, and review preferences.
*   **Command Line Arguments:** For initiating on-demand reviews of specific pull requests (repository URL, PR number).

**Outputs:**

*   **GitHub Pull Request Comments:** Posts inline comments on specific lines of code with detailed findings and suggestions.
*   **GitHub Pull Request Summary:** Provides a summary comment on the pull request outlining all detected issues.
*   **GitHub Pull Request Approval:** Optionally approves pull requests when no issues are found.
*   **Console Output:** Logs agent activities and review progress.

**Configuration:**

The agent's behavior is controlled through environment variables, typically loaded from a `.env` file. Key configuration options include:

*   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
*   `AI_PROVIDER`: Specifies the AI service (e.g., `openai`, `anthropic`).
*   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
*   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
*   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
*   `AUTO_APPROVE_MINOR`: Set to `true` to enable automatic approval of clean PRs.
*   `AGENT_NAME`: The name used by the agent when posting comments.
*   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.