### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews, providing feedback directly on GitHub.

#### Key Features
*   **Automated Code Review**: Automatically reviews pull requests for various issues.
*   **Typo and Grammar Detection**: Identifies and suggests corrections for spelling and grammar errors in code and documentation.
*   **AI-Powered Code Quality Analysis**: Utilizes AI models (OpenAI or Anthropic) to assess code quality, adherence to best practices, and potential bugs.
*   **Security Vulnerability Scanning**: Detects common security vulnerabilities such as hardcoded secrets, SQL injection risks, and command injection.
*   **GitHub Integration**: Posts detailed review comments directly on pull requests, including inline suggestions and a summary.
*   **Configurable Review Types**: Allows users to enable or disable specific review types (typos, code quality, security).
*   **Automatic Approval**: Can be configured to automatically approve pull requests where no issues are found.
*   **Flexible Operation**: Can operate in a continuous polling mode to monitor multiple repositories or review a single, specific pull request on demand.
*   **Dry Run Mode**: Supports a dry run mode to preview review comments without posting them to GitHub.

#### Inputs
*   **GitHub API (HTTP)**: Fetches pull request details, files, and existing comments from specified repositories.
*   **Environment Variables**: Configures agent behavior, GitHub authentication, AI provider details, and review settings (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `MAX_FILES_PER_REVIEW`).
*   **Command Line Arguments (stdin)**: For on-demand review of a single PR, takes repository URL and PR number.

#### Outputs
*   **GitHub API (HTTP)**: Posts new comments on pull requests (inline comments on specific lines, and summary comments).
*   **Console (stdout)**: Provides logs and status updates on agent operations.

#### Configuration
The agent is highly configurable through environment variables, allowing users to:
*   Specify GitHub Personal Access Token and watched repositories.
*   Choose between OpenAI or Anthropic as the AI provider and provide corresponding API keys.
*   Toggle review types (typos, code quality, security).
*   Set limits on the number of files and lines reviewed per pull request.
*   Configure agent name and polling interval.