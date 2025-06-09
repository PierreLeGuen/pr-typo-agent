### PR Review Agent

The PR Review Agent is an AI-powered automation tool designed to enhance code review processes on GitHub. It continuously monitors specified repositories for new or updated pull requests and performs automated reviews based on configurable criteria, providing immediate feedback to developers.

#### Main Functions

*   **Automated Pull Request Monitoring**: Watches configured GitHub repositories for new or open pull requests that require review.
*   **Comprehensive Code Analysis**:
    *   **Typo and Grammar Detection**: Identifies spelling and grammatical errors in added code lines, offering AI-generated suggestions for correction.
    *   **AI-Powered Code Quality Review**: Utilizes large language models (OpenAI or Anthropic) to assess code for quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Scanning**: Detects common security issues such as hardcoded secrets, potential SQL injection, command injection, and usage of weak cryptographic algorithms.
*   **GitHub Integration**: Posts detailed feedback directly on pull requests, including inline comments for specific issues and a comprehensive summary comment.
*   **Configurable Review Behavior**: Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the size of PRs and files to be reviewed.
*   **On-Demand Review**: Supports reviewing a specific pull request manually by providing its repository URL and PR number.
*   **Interactive Setup**: Provides a command-line utility for initial configuration, simplifying the setup of necessary API keys and settings.

#### Inputs

*   **Configuration (Environment Variables)**: The agent's behavior and access credentials are configured through environment variables, typically loaded from a `.env` file. These include GitHub tokens, AI provider API keys, watched repositories, review preferences (e.g., `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`), and operational parameters (e.g., `POLLING_INTERVAL`, `MAX_FILES_PER_REVIEW`).
*   **GitHub Pull Request Data (HTTP)**: The agent fetches pull request details, file changes (diffs), and existing comments directly from the GitHub API.
*   **Command-Line Arguments (stdin)**: Users interact with the agent via command-line arguments to start monitoring, review a specific PR, or run the setup utility.

#### Outputs

*   **GitHub Comments (HTTP)**: The primary output is automated comments posted on GitHub pull requests. This includes:
    *   Inline review comments on specific lines of code where issues are detected.
    *   A summary comment on the pull request detailing the findings.
    *   An approval comment if no issues are found (configurable).
*   **Console Output (stdout)**: Provides real-time status updates, logging information, and error messages during the agent's operation.