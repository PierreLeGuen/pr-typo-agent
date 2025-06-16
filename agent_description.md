### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews, providing feedback directly on GitHub.

#### Functionality

*   **Automated Code Review**: Automatically reviews new or specified pull requests for various issues.
*   **Typo and Grammar Detection**: Identifies and suggests corrections for spelling and grammar errors in code comments, documentation, and string literals within changed files.
*   **AI-Powered Code Quality Analysis**: Utilizes advanced AI models (OpenAI or Anthropic) to assess code quality, readability, performance, and adherence to best practices.
*   **Security Vulnerability Scanning**: Detects potential security risks such as hardcoded secrets, SQL injection vulnerabilities, command injection, and weak cryptographic algorithms.
*   **GitHub Integration**: Posts detailed review comments inline on specific lines of code where issues are found, and provides a summary comment for the entire pull request.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Flexible Monitoring**: Operates by polling configured GitHub repositories at a set interval or can be triggered to review a specific pull request on demand.
*   **Configurable Review Scope**: Allows users to set limits on the maximum number of files and lines reviewed per pull request.

#### Inputs

*   **Environment Variables**: Configuration settings loaded from the environment or a `.env` file, including GitHub API tokens, AI service API keys, watched repositories, and various review preferences.
*   **GitHub API**: Receives pull request data, file changes (diffs), and existing comments from monitored GitHub repositories.
*   **Command Line**: Accepts repository URL and pull request number for on-demand reviews.

#### Outputs

*   **GitHub API**: Posts new comments on pull requests, including inline review comments for specific code lines and summary comments for the entire PR.
*   **Stdout/Logs**: Outputs operational status, detected issues, and error messages to the console or logs.

#### Configuration

The agent's behavior is highly configurable via environment variables, allowing users to:
*   Choose between OpenAI and Anthropic for AI services.
*   Enable or disable specific review types (typos, code quality, security).
*   Set the agent's name for comments.
*   Define the polling interval for new PRs.
*   Specify repositories to monitor.
*   Control auto-approval behavior.