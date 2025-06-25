### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new pull requests and performs comprehensive analysis to identify potential issues related to code quality, security vulnerabilities, and grammatical/spelling errors. The agent then provides detailed feedback by posting comments directly on the pull request or, if configured, automatically approves PRs with no issues.

**Key Features:**

*   **Automated PR Monitoring**: Continuously checks designated GitHub repositories for new pull requests.
*   **AI-Powered Code Review**: Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for quality, best practices, and potential bugs.
*   **Security Vulnerability Detection**: Scans code for common security risks such as hardcoded secrets, SQL injection, and command injection.
*   **Typo and Grammar Correction**: Reviews newly added lines of code and documentation for spelling and grammatical errors, suggesting corrections.
*   **Configurable Review Scope**: Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **Direct GitHub Interaction**: Posts detailed inline comments on specific lines of code and comprehensive summary comments on the pull request timeline.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests where no issues are found.
*   **Flexible Operation**: Can operate in a continuous polling mode to monitor repositories or be invoked to review a specific pull request on demand.
*   **Dry Run Mode**: Supports a dry-run mode to preview review comments without actually posting them to GitHub.

**Inputs:**

*   **Configuration**: The agent's behavior is configured via environment variables, typically loaded from a `.env` file. These include:
    *   **GitHub Token**: A Personal Access Token with `repo` permissions for GitHub API authentication.
    *   **AI Provider & Keys**: Selection of AI service ("openai" or "anthropic") and corresponding API keys.
    *   **Review Settings**: Booleans to enable/disable typo, code quality, and security reviews.
    *   **Behavior Settings**: Flags for auto-approval, maximum files/lines per review.
    *   **Repository Monitoring**: A comma-separated list of GitHub repositories to watch.
    *   **Agent Name**: The name used for comments posted by the agent.
    *   **Polling Interval**: Frequency (in seconds) for checking new PRs.
*   **GitHub Pull Request Data**: The agent fetches pull request details, including changed files and their content (patches), from monitored repositories via the GitHub API.
*   **Command-line Arguments**:
    *   `start`: Initiates continuous monitoring.
    *   `review <repo_url> <pr_number>`: Reviews a specific pull request.

**Outputs:**

*   **GitHub Pull Request Comments**: Posts detailed feedback as inline comments on specific lines of code and as a summary comment on the pull request.
*   **GitHub Pull Request Approvals**: Submits an approval status to the pull request if no issues are detected and auto-approval is enabled.
*   **Console/Log Output**: Provides real-time operational logs and status updates to the standard output.