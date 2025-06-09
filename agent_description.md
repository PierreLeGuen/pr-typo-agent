### Name
PR Review Agent

### Description
The PR Review Agent is an AI-powered automation tool designed to monitor GitHub repositories and provide automated feedback on Pull Requests. It performs comprehensive code reviews, identifying potential issues related to typos, code quality, and security vulnerabilities, and then posts detailed comments directly on the Pull Request.

### Functions
*   **Automated PR Monitoring**: Continuously monitors a configurable list of GitHub repositories for new or updated open Pull Requests.
*   **Multi-faceted Code Review**:
    *   **Typo and Grammar Check**: Analyzes new code additions for spelling and grammatical errors, offering suggestions for correction.
    *   **AI-Powered Code Quality Review**: Utilizes large language models (OpenAI or Anthropic) to assess code quality, adherence to best practices, potential performance bottlenecks, and logical bugs.
    *   **Security Vulnerability Detection**: Scans code for common security flaws such as hardcoded secrets, potential SQL injection, command injection, and use of weak cryptographic algorithms.
*   **Intelligent Commenting**: Posts inline comments on specific lines of code where issues are detected, along with a comprehensive summary comment on the Pull Request.
*   **Configurable Behavior**: Allows users to enable/disable specific review types, set limits on file and line changes for review, and configure the agent's polling interval.
*   **On-Demand Review**: Can be triggered to review a specific Pull Request manually.
*   **Dry Run Mode**: Supports a dry run mode to preview comments without actually posting them to GitHub.
*   **Optional Auto-Approval**: Can be configured to automatically approve Pull Requests if no issues are found during the review.

### Inputs
*   **Configuration (Environment Variables/`.env` file)**:
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Choice of AI service (e.g., "openai", "anthropic").
    *   `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag for automatic PR approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for review scope.
    *   `POLLING_INTERVAL`: Frequency for checking new PRs.
    *   `AGENT_NAME`: The name used for comments posted by the agent.
*   **GitHub Data (HTTP)**: Pull Request details, file changes (diffs), and existing comments retrieved from the GitHub API.
*   **Command Line Arguments (stdin)**: For the `review` command, takes `repo_url` and `pr_number` as arguments.

### Outputs
*   **GitHub Comments (HTTP)**: Posts inline review comments on specific lines within Pull Requests and a summary comment on the overall PR.
*   **GitHub PR Approval (HTTP)**: If configured, can approve Pull Requests.
*   **Console Output (stdout)**: Provides logging and status messages during operation.