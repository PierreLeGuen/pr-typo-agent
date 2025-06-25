## PR Review Agent

An AI-powered agent designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests, performs comprehensive reviews, and provides feedback directly on GitHub.

### Main Functions

*   **Automated PR Review**: Monitors configured GitHub repositories for new pull requests and initiates reviews.
*   **AI-Powered Code Analysis**: Utilizes AI models (OpenAI or Anthropic) to assess code quality, identify potential bugs, and suggest improvements.
*   **Typo and Grammar Checking**: Scans new code and comments for spelling and grammar errors, offering corrections.
*   **Security Vulnerability Detection**: Identifies common security patterns and potential vulnerabilities within the code.
*   **GitHub Integration**: Posts detailed review comments directly on the pull request, including inline comments for specific lines and a summary comment.
*   **Conditional Approval**: Can be configured to automatically approve pull requests if no issues are detected.
*   **On-Demand Review**: Supports reviewing a specific pull request by providing its repository URL and PR number.

### Key Features

*   **Configurable Review Types**: Enable or disable typo, code quality, and security reviews based on project needs.
*   **Customizable Scope**: Set limits on the maximum number of files and lines reviewed per pull request.
*   **Flexible AI Providers**: Choose between OpenAI and Anthropic for AI-driven analysis.
*   **Polling or Webhook (Planned)**: Operates by polling GitHub for new PRs at a configurable interval. (Note: Webhook secret is present in config, suggesting future webhook support).
*   **Customizable Agent Name**: Define the name used by the agent when posting comments.

### Inputs

*   **Environment Variables**: Configuration parameters provided via environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`).
*   **GitHub API**: Fetches pull request details, changed files, and existing comments from GitHub.
*   **Command Line Arguments (for `review` command)**: Repository URL and PR number for on-demand reviews.

### Outputs

*   **GitHub Comments**: Posts inline comments on specific lines of code and a comprehensive summary comment on the pull request.
*   **GitHub Approvals**: Issues a "Review Complete" comment and potentially approves the PR if `AUTO_APPROVE_MINOR` is enabled and no issues are found.
*   **Console/Logs**: Provides operational logs and status updates to the standard output.