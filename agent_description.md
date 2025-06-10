### Name
PR Review Agent

### Description
The PR Review Agent is an AI-powered tool designed to automate and enhance pull request reviews on GitHub. It actively monitors specified repositories for new or updated pull requests and performs automated checks for various aspects of code quality, security, and readability.

### Functions
*   **Automated PR Monitoring**: Continuously monitors configured GitHub repositories for open pull requests that require review.
*   **Comprehensive Code Review**: Conducts multi-faceted reviews including:
    *   **Typo and Grammar Detection**: Identifies and suggests corrections for spelling and grammatical errors in new or modified code.
    *   **AI-Powered Code Quality Assessment**: Leverages advanced AI models (OpenAI or Anthropic) to evaluate code for quality, readability, adherence to best practices, and potential performance issues.
    *   **Security Vulnerability Scanning**: Detects common security risks such as hardcoded secrets, SQL injection vulnerabilities, command injection flaws, and the use of weak cryptographic algorithms.
*   **GitHub Integration**: Posts detailed findings as inline comments on specific lines of code and provides a comprehensive summary comment on the pull request. It can also automatically approve pull requests if no issues are detected.
*   **Configurable Review Scope**: Allows users to define limits on the number of files and lines reviewed per pull request to manage review complexity.
*   **On-Demand Review**: Supports reviewing a specific pull request by its repository URL and pull request number, independent of continuous monitoring.
*   **Interactive Setup**: Provides a command-line utility to guide users through the initial configuration process.

### Inputs
*   **Configuration (Environment Variables)**: The agent's behavior is configured via environment variables, typically loaded from a `.env` file. These include:
    *   GitHub Personal Access Token (`GITHUB_TOKEN`)
    *   AI Provider selection (`AI_PROVIDER`) and corresponding API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`)
    *   Flags to enable/disable specific review types (`REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`)
    *   Behavioral settings like auto-approval (`AUTO_APPROVE_MINOR`), review limits (`MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`)
    *   List of repositories to monitor (`WATCHED_REPOSITORIES`)
    *   Agent's display name (`AGENT_NAME`) and polling interval (`POLLING_INTERVAL`)
*   **GitHub Pull Request Data (HTTP)**: The agent fetches pull request details, changed files, and patch content directly from the GitHub API.
*   **Command-line Arguments (stdin)**:
    *   **`start` command**: Accepts optional flags for configuration file path, dry-run mode, and verbose logging.
    *   **`review` command**: Requires a repository URL and pull request number, with optional flags for configuration file path and dry-run mode.
    *   **`setup` command**: Prompts for required configuration values interactively.

### Outputs
*   **GitHub Comments (HTTP)**:
    *   **Inline Review Comments**: Posts comments directly on specific lines of code within the pull request, highlighting issues and suggesting improvements.
    *   **Summary Comments**: Provides a consolidated summary of all findings at the pull request level.
    *   **Approval Comments**: Posts a celebratory comment indicating a clean review if no issues are found and auto-approval is enabled.
*   **Console Output (stdout)**: Displays agent status, operational logs, error messages, and interactive setup prompts.