### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews, identifying issues related to code quality, security, and typos. Based on its findings, the agent posts detailed comments or approves the pull request.

#### Key Features
*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Quality Review**: Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for best practices, potential bugs, and overall quality.
*   **Security Vulnerability Detection**: Scans code for common security issues such as hardcoded secrets, SQL injection risks, and command injection vulnerabilities.
*   **Typo and Grammar Correction**: Reviews newly added or modified lines of code for spelling and grammatical errors, suggesting corrections.
*   **Actionable Feedback**: Posts detailed inline comments directly on specific lines of code and provides a comprehensive summary comment on the pull request.
*   **Configurable Behavior**: Allows users to enable/disable specific review types (typos, code quality, security), set limits on the number of files and lines reviewed, and configure automatic approvals for clean pull requests.
*   **On-Demand Review**: Can be manually triggered to review a specific pull request by its repository URL and number.

#### Configuration
The agent is configured using environment variables, typically loaded from a `.env` file. This includes:
*   **GitHub Token**: For authentication with the GitHub API.
*   **AI Provider & API Key**: To select and authenticate with either OpenAI or Anthropic for AI-driven reviews.
*   **Watched Repositories**: A list of GitHub repositories to monitor.
*   **Review Settings**: Flags to enable/disable typo, code quality, and security reviews, along with limits for review scope.
*   **Polling Interval**: How frequently the agent checks for new PRs.

#### Inputs
*   **GitHub API**: Pull request details, file changes (diffs), and existing comments.
*   **Environment Variables**: Configuration parameters (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`).
*   **Command Line Interface (CLI)**: Specific repository URL and pull request number for on-demand reviews.

#### Outputs
*   **GitHub API**: Posts comments (inline and summary) on pull requests and can issue approvals.
*   **Standard Output (stdout)**: Provides operational logs and status updates during execution.