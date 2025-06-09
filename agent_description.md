### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new pull requests and provides automated feedback on various aspects, including typos, code quality, and potential security vulnerabilities.

#### Main Functions

*   **Automated Pull Request Review**: The agent continuously monitors configured GitHub repositories for new or updated pull requests.
*   **On-Demand PR Review**: Users can also trigger a review for a specific pull request by providing its repository URL and PR number.
*   **Comprehensive Review Capabilities**:
    *   **Typo and Grammar Detection**: Identifies spelling and grammar errors in code comments, documentation, and string literals, optionally leveraging an AI model for suggestions.
    *   **AI-Powered Code Quality Review**: Utilizes large language models (LLMs) from providers like OpenAI or Anthropic to analyze code for quality, best practices, performance issues, and potential bugs.
    *   **Security Vulnerability Scanning**: Detects common security risks such as hardcoded secrets, potential SQL injection, command injection, and use of weak cryptographic algorithms.
*   **Intelligent Filtering**: Automatically skips draft PRs, PRs that have already been reviewed by the agent, and PRs that exceed configurable file or line limits.
*   **Detailed Feedback**: Posts findings as inline comments on specific lines of code and provides a comprehensive summary comment on the pull request.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests if no issues are found during the review.
*   **Interactive Setup**: Includes a command-line utility for easy initial configuration of GitHub and AI API keys.

#### Inputs

*   **Configuration**: Environment variables (typically loaded from a `.env` file), including GitHub tokens, AI API keys, watched repositories, and review preferences.
*   **GitHub Pull Requests**: The agent fetches PR details, changed files, and existing comments via the GitHub API (HTTP).
*   **Command Line Arguments**: Used to specify the configuration file, enable dry-run mode, set verbosity, or trigger a review for a specific PR (repository URL, PR number).

#### Outputs

*   **GitHub Comments**: The agent posts review comments (inline for specific issues and a summary comment for the entire PR) directly on GitHub pull requests via the GitHub API (HTTP).
*   **Console Output**: Logs agent activity, errors, and setup messages to standard output (stdout).