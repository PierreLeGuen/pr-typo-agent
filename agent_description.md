### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the pull request review process on GitHub. It monitors specified repositories for new pull requests and performs comprehensive reviews, providing feedback directly on GitHub.

#### Functionality

*   **Automated PR Review**: Continuously monitors designated GitHub repositories for new or updated pull requests.
*   **Typo and Grammar Detection**: Identifies spelling and grammar errors in code comments, documentation, and string literals, suggesting corrections.
*   **AI-Powered Code Quality Review**: Utilizes large language models (LLMs) to analyze code for quality, readability, performance issues, and best practice violations.
*   **Security Vulnerability Scanning**: Scans code for common security risks such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **Detailed Feedback**: Posts inline comments on specific lines of code where issues are found and provides a summary comment for the entire pull request.
*   **Configurable Behavior**: Allows users to enable/disable specific review types (typos, code quality, security), set limits on file and line review counts, and configure polling intervals.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests where no issues are detected.
*   **Single PR Review**: Supports reviewing a specific pull request on demand, in addition to continuous monitoring.

#### Inputs

*   **GitHub API (Polling)**: The agent periodically fetches open pull requests and their associated files and comments from configured GitHub repositories.
*   **CLI Arguments (stdin)**:
    *   `start`: Initiates continuous monitoring of configured repositories.
    *   `review <repo_url> <pr_number>`: Triggers a review for a specific pull request.
    *   `setup`: Guides users through interactive configuration.
*   **Environment Variables**: Configuration parameters loaded from a `.env` file or system environment, including GitHub tokens, AI API keys, and review preferences.

#### Outputs

*   **GitHub PR Comments**: Posts inline comments on specific lines of code with identified issues (typos, code quality suggestions, security warnings).
*   **GitHub PR Summary Comments**: Adds a comprehensive summary comment to the pull request, detailing the types and counts of issues found or confirming a clean review.
*   **GitHub PR Approval**: Optionally approves pull requests if no issues are detected and auto-approval is enabled.
*   **Console Output (stdout)**: Provides logs and status updates on the agent's operations, including errors and review progress.

#### Configuration

The agent is configured using environment variables, typically loaded from a `.env` file. Key configurable parameters include:

*   `GITHUB_TOKEN`: Your GitHub Personal Access Token.
*   `AI_PROVIDER`: Choice of AI model provider (e.g., `openai`, `anthropic`).
*   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
*   `REVIEW_TYPOS`: Enable/disable typo review.
*   `REVIEW_CODE_QUALITY`: Enable/disable AI-powered code quality review.
*   `REVIEW_SECURITY`: Enable/disable security review.
*   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
*   `AGENT_NAME`: The name displayed in PR comments.
*   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
*   `MAX_FILES_PER_REVIEW`: Maximum files to review per PR.
*   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
*   `AUTO_APPROVE_MINOR`: Enable/disable auto-approval for clean PRs.