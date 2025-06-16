**Name:** PR Review Agent

**Summary:**
The PR Review Agent is an AI-powered bot designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests, or can be triggered to review a specific PR. The agent performs comprehensive checks, including AI-driven code quality analysis, typo and grammar detection, and security vulnerability scanning. Based on its findings, it posts detailed review comments directly on the pull request, providing actionable feedback or an approval if no issues are found.

**Key Capabilities:**
*   **Automated PR Monitoring:** Watches designated GitHub repositories for new pull requests at a configurable interval.
*   **On-Demand Review:** Allows for manual triggering of a review for any specific pull request via a command-line interface.
*   **AI-Powered Code Quality:** Utilizes advanced AI models (configurable for OpenAI or Anthropic) to analyze code for best practices, potential bugs, and performance issues.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors in code and documentation.
*   **Security Vulnerability Detection:** Scans for common security flaws such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
*   **Detailed Feedback:** Posts inline comments on specific lines of code and a summary comment for the entire pull request on GitHub.
*   **Configurable Reviews:** Enables or disables specific review types (typos, code quality, security) based on project needs.
*   **Automatic Approval (Optional):** Can be configured to automatically approve pull requests where no issues are detected.
*   **Scalable Review Limits:** Configurable limits on the maximum number of files and lines reviewed per pull request to manage scope.

**Inputs:**
*   **GitHub API (HTTP):** Fetches pull request details, file changes (diffs), and existing comments from monitored repositories.
*   **Environment Variables (System/File):** Configuration settings such as GitHub token, AI provider API keys, watched repositories, and review preferences are loaded from environment variables or a `.env` file.
*   **Command Line Arguments (stdin):** For on-demand reviews, the repository URL and pull request number are provided as arguments.

**Outputs:**
*   **GitHub Pull Request Comments (HTTP):** Posts new comments directly on GitHub pull requests, including inline suggestions and a summary of findings.
*   **Console Logs (stdout):** Provides real-time status updates, warnings, and errors to the console.

**Configuration:**
The agent's behavior is highly configurable through the following environment variables:
*   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
*   `AI_PROVIDER`: Specifies the AI service to use for reviews (e.g., `openai`, `anthropic`).
*   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
*   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
*   `REVIEW_TYPOS`: Set to `true` to enable typo and grammar review.
*   `REVIEW_CODE_QUALITY`: Set to `true` to enable AI-powered code quality review.
*   `REVIEW_SECURITY`: Set to `true` to enable security vulnerability review.
*   `AUTO_APPROVE_MINOR`: Set to `true` to automatically approve pull requests with no issues found.
*   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
*   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
*   `AGENT_NAME`: The name that appears in PR comments (defaults to "PR Review Bot").
*   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
*   `GITHUB_WEBHOOK_SECRET`: Optional secret for GitHub webhook validation.
*   `MAX_RETRIES`: Maximum retries for API calls.