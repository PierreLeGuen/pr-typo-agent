### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and provides automated feedback based on configurable review types.

#### Description
This agent streamlines development workflows by performing automated checks on pull requests, identifying potential issues before human review. It aims to improve code quality, security, and maintain consistency across projects.

#### Functions
*   **Automated PR Monitoring**: Periodically checks configured GitHub repositories for new or updated pull requests.
*   **Comprehensive Code Review**:
    *   **Typo and Grammar Detection**: Identifies spelling and grammar errors in code comments, documentation, and string literals, optionally using AI for advanced corrections.
    *   **AI-powered Code Quality Review**: Utilizes large language models (OpenAI or Anthropic) to assess code for best practices, readability, performance issues, and potential bugs.
    *   **Security Vulnerability Detection**: Scans for common security patterns such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **GitHub Interaction**: Fetches PR details, files, and comments, and posts review comments directly on GitHub, including inline suggestions and a summary comment.
*   **Configurable Behavior**: Allows users to enable/disable specific review types, set limits on file/line review size, and configure polling intervals.
*   **Manual PR Review**: Supports on-demand review of a specific pull request via a command-line interface.
*   **Configuration Setup**: Provides an interactive command-line utility to simplify the initial setup of environment variables.

#### Inputs
*   **Configuration**: Environment variables loaded from a `.env` file or directly from the system, including GitHub API tokens, AI provider keys, and review preferences (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `REVIEW_TYPOS`, `WATCHED_REPOSITORIES`).
*   **GitHub Pull Requests**: The agent processes open pull requests from monitored repositories.
*   **CLI Arguments**: For manual review, the agent accepts a repository URL and PR number (e.g., `pr-review-agent review <repo_url> <pr_number>`).

#### Outputs
*   **GitHub PR Comments**: The agent posts detailed review comments directly on GitHub pull requests. This includes:
    *   Inline comments with specific findings (typos, code quality issues, security concerns) and suggested improvements.
    *   A summary comment on the pull request, outlining the types and counts of issues found.
    *   An approval comment if no issues are detected.
*   **Console Output**: Provides real-time logging and status updates to the console during operation.