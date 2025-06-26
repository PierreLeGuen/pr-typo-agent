### Name
PR Review Agent

### Summary
The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests, automatically fetching changes and applying various review checks.

### Key Features
*   **Automated Code Review**: Conducts AI-powered analysis of code changes for quality, best practices, and potential bugs using either OpenAI or Anthropic models.
*   **Typo and Grammar Checking**: Reviews new code and comments for spelling and grammar errors, providing suggestions for correction.
*   **Security Vulnerability Detection**: Identifies common security issues such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **Intelligent Feedback**: Posts detailed inline comments directly on GitHub for specific issues found, along with a comprehensive summary comment for each reviewed pull request.
*   **Configurable Behavior**: Allows users to enable/disable specific review types (typos, code quality, security), set limits on file and line review sizes, and configure automatic approval for PRs with no issues.
*   **Flexible Operation**: Can operate in a continuous polling mode to monitor multiple repositories or be triggered to review a specific pull request on demand.

### Inputs
*   **GitHub API**: Pull request data, including file changes (diffs), existing comments, and PR metadata, fetched from monitored repositories.
*   **Command Line**: Repository URL and pull request number for on-demand review of a specific PR.

### Outputs
*   **GitHub Comments**: Posts inline comments on specific lines of code within a pull request and adds summary comments to the overall pull request discussion.
*   **GitHub Approvals**: Can post an approval comment on a pull request if no issues are detected and the `AUTO_APPROVE_MINOR` setting is enabled.

### Configuration
The agent's behavior is configured via environment variables:
*   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
*   `AI_PROVIDER`: AI service provider ("openai" or "anthropic").
*   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
*   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
*   `REVIEW_TYPOS`: Enables/disables typo review (`true`/`false`).
*   `REVIEW_CODE_QUALITY`: Enables/disables AI code quality review (`true`/`false`).
*   `REVIEW_SECURITY`: Enables/disables security review (`true`/`false`).
*   `AUTO_APPROVE_MINOR`: Enables/disables automatic approval for clean PRs (`true`/`false`).
*   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
*   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
*   `AGENT_NAME`: The name used by the agent when posting comments (defaults to "PR Review Bot").
*   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
*   `MAX_RETRIES`: Maximum retries for API calls.
*   `GITHUB_WEBHOOK_SECRET`: Optional secret for GitHub webhook validation.