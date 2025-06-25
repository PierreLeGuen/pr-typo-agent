## PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the pull request review process on GitHub. It monitors specified repositories for new pull requests and performs comprehensive code reviews, providing feedback directly on GitHub.

### Main Functions

*   **Automated PR Monitoring**: Continuously checks designated GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review**: Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for:
    *   **Code Quality**: Identifies best practice violations, potential bugs, and areas for improvement.
    *   **Security Vulnerabilities**: Detects common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
    *   **Typos and Grammar**: Reviews code comments, documentation, and string literals for spelling and grammatical errors.
*   **Detailed Feedback**: Posts inline comments on specific lines of code where issues are found, along with suggestions for correction. It also provides a summary comment for the entire pull request.
*   **Selective Review**: Allows users to enable or disable specific review types (typos, code quality, security) based on their needs.
*   **Configurable Behavior**: Supports customization for review scope (maximum files/lines per review), automatic approval of clean PRs, and the agent's display name.
*   **On-Demand Review**: Can be invoked to review a specific pull request manually via a command-line interface.

### Inputs

*   **GitHub Pull Requests**: The agent processes changes within open pull requests from configured repositories.
*   **Environment Variables**: Configuration is provided through environment variables, typically loaded from a `.env` file. These include:
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: The AI service to use ("openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable automatic approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits the scope of review.
    *   `AGENT_NAME`: The name displayed in PR comments.
    *   `POLLING_INTERVAL`: How often the agent checks for new PRs (in seconds).
*   **CLI Arguments**: For on-demand reviews, `repo_url` and `pr_number` are provided via command-line.

### Outputs

*   **GitHub Comments**: The agent posts review comments, suggestions, and summary reports directly on the GitHub pull request interface.
*   **GitHub PR Approvals**: If configured and no issues are found, the agent can approve the pull request.
*   **Console/Standard Output**: Provides logging information, status updates, and error messages during operation.