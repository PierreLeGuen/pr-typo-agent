### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate the review process for GitHub pull requests. It continuously monitors specified repositories for new PRs, applying configurable checks for code quality, security vulnerabilities, and typos. Based on its findings, the agent posts detailed comments directly on the pull request, including inline suggestions, and can optionally approve PRs that pass all checks.

**Main Functions:**
*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review:** Utilizes AI models (OpenAI or Anthropic) to assess code quality, identify potential issues, and suggest improvements.
*   **Typo and Grammar Detection:** Reviews new code and comments for spelling and grammar errors.
*   **Security Vulnerability Scanning:** Identifies common security patterns and potential vulnerabilities within the code.
*   **Detailed Feedback:** Posts inline comments on specific lines of code where issues are found, along with a comprehensive summary comment on the pull request.
*   **Automated Approval:** Can be configured to automatically approve pull requests that pass all configured review checks without any issues.
*   **Configurable Scope:** Allows setting limits on the number of files and lines reviewed per pull request.

**Inputs:**
*   **Medium:** Environment Variables
*   **Details:**
    *   `GITHUB_TOKEN`: A GitHub Personal Access Token with `repo` permissions for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service provider to use (e.g., "openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
    *   `REVIEW_TYPOS`: Boolean flag to enable or disable typo and grammar review.
    *   `REVIEW_CODE_QUALITY`: Boolean flag to enable or disable AI-powered code quality review.
    *   `REVIEW_SECURITY`: Boolean flag to enable or disable security vulnerability review.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable or disable automatic approval for pull requests with no issues.
    *   `POLLING_INTERVAL`: The frequency (in seconds) at which the agent checks for new pull requests.
    *   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum number of lines to review per file.
    *   `AGENT_NAME`: The name the agent uses when posting comments.

**Outputs:**
*   **Medium:** GitHub Pull Request Comments and Status
*   **Details:**
    *   Inline comments on specific lines within a pull request, highlighting detected issues (e.g., typos, code quality suggestions, security concerns) with suggested fixes.
    *   A summary comment posted on the pull request, providing an overview of findings or confirming that no issues were detected.
    *   Optional pull request approval if `AUTO_APPROVE_MINOR` is enabled and no issues are found.