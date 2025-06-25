### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews, identifying potential issues related to code quality, security vulnerabilities, and typos. Based on its findings, the agent posts detailed comments or approves the pull request directly on GitHub.

**Capabilities:**

*   **Automated PR Monitoring:** Regularly checks configured GitHub repositories for new or updated pull requests.
*   **Intelligent Code Review:** Utilizes AI models (OpenAI or Anthropic) to analyze code changes for quality, readability, performance, and best practices.
*   **Security Vulnerability Detection:** Scans code for common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors in code comments, documentation, and string literals.
*   **Detailed Feedback:** Posts inline comments on specific lines of code where issues are found, along with a summary comment on the pull request.
*   **Configurable Approvals:** Can be set to automatically approve pull requests if no issues are detected during the review.
*   **Customizable Review Scope:** Allows users to enable/disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **On-Demand Review:** Supports reviewing a specific pull request manually via a command-line interface.

**Inputs:**

*   **Environment Variables:**
    *   `GITHUB_TOKEN`: A GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: Specifies the AI service provider ("openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags (`true`/`false`) to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag (`true`/`false`) for auto-approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `AGENT_NAME`: The name used by the agent in PR comments.
    *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
*   **Command Line (for on-demand review):**
    *   `repo_url`: The URL of the GitHub repository.
    *   `pr_number`: The specific pull request number.

**Outputs:**

*   **GitHub Comments:**
    *   Inline comments on specific lines within a pull request, detailing findings (e.g., typos, code quality issues, security risks) with suggestions.
    *   A summary comment on the pull request, listing the types and counts of issues found.
    *   An approval comment if no issues are detected and auto-approval is enabled.
*   **Console Logs:** Provides real-time status updates and error messages.