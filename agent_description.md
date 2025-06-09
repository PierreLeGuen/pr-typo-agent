### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews, providing immediate feedback directly on the PR.

#### Main Functions

*   **Automated PR Monitoring**: Watches configured GitHub repositories for new and updated pull requests.
*   **Multi-faceted Code Review**:
    *   **Typo and Grammar Check**: Identifies spelling and grammatical errors in new code and comments, offering suggestions for correction.
    *   **AI-Powered Code Quality Review**: Utilizes large language models (OpenAI or Anthropic) to assess code for quality, adherence to best practices, potential performance issues, and general bugs.
    *   **Security Vulnerability Detection**: Scans for common security risks such as hardcoded secrets, potential SQL injection, command injection, and use of weak cryptographic algorithms.
*   **Intelligent Feedback**: Posts detailed inline comments on specific lines where issues are found, along with a comprehensive summary comment on the pull request.
*   **Configurable Behavior**: Allows users to enable/disable specific review types, set limits on file and line review sizes, and configure polling intervals.
*   **On-Demand Review**: Can be triggered to review a specific pull request manually.

#### Inputs

*   **Environment Variables / Configuration File (`.env`)**:
    *   `GITHUB_TOKEN`: A GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Choice of AI service (`openai` or `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor (e.g., `owner/repo`).
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable or disable specific review features.
    *   `AGENT_NAME`: The name used by the agent in its comments.
    *   `POLLING_INTERVAL`: How often the agent checks for new PRs (in seconds).
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits on the size of PRs/files to review.
*   **GitHub Pull Requests**: Reads PR details, file changes (diffs), and existing comments from monitored repositories.
*   **Command Line Arguments (for `review` command)**:
    *   `repo_url`: The URL of the GitHub repository.
    *   `pr_number`: The specific pull request number to review.

#### Outputs

*   **GitHub PR Comments**:
    *   **Inline Comments**: Posted directly on specific lines within the PR's changed files, detailing identified issues (typos, code quality, security) with suggestions.
    *   **Summary Comments**: A general comment posted on the PR providing an overview of the review findings or an approval message if no issues are detected.
*   **Console Logs**: Provides real-time feedback on agent activities, including monitoring status, PR review progress, and any errors encountered.