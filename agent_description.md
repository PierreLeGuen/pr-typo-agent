### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It monitors specified repositories for new pull requests and performs comprehensive reviews, providing feedback on code quality, security vulnerabilities, and potential typos.

#### Key Functions

*   **Automated Pull Request Review**: Continuously monitors designated GitHub repositories for new pull requests or can be triggered to review a specific PR.
*   **Multi-faceted Review**:
    *   **Code Quality**: Utilizes AI models (OpenAI or Anthropic) to analyze code for best practices, readability, performance issues, and potential bugs.
    *   **Security Analysis**: Identifies common security vulnerabilities such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
    *   **Typo and Grammar Check**: Reviews code comments, documentation, and string literals for spelling and grammatical errors.
*   **Intelligent Feedback**: Posts detailed inline comments on specific lines where issues are detected, including suggestions for improvement.
*   **Summary Reporting**: Provides a comprehensive summary comment on the pull request, outlining all findings.
*   **Conditional Approval**: Can be configured to automatically approve pull requests if no issues are found.
*   **Configurable Behavior**: Allows users to enable/disable specific review types, set review thresholds (max files/lines), and define polling intervals.

#### Inputs

*   **Environment Variables**: Configured via environment variables (or a `.env` file) for:
    *   GitHub authentication (`GITHUB_TOKEN`).
    *   AI provider selection (`AI_PROVIDER`) and API keys (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`).
    *   Repositories to monitor (`WATCHED_REPOSITORIES`).
    *   Review preferences (e.g., `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AUTO_APPROVE_MINOR`).
    *   Performance limits (e.g., `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`).
*   **GitHub API (HTTP)**: Pull request details, file changes (diffs), and existing comments from monitored repositories.
*   **Command Line (stdin)**: For reviewing a specific PR, the repository URL and pull request number are provided as arguments.

#### Outputs

*   **GitHub API (HTTP)**:
    *   Inline comments on specific lines within pull requests.
    *   Summary comments posted on the main pull request thread.
    *   Potential pull request approvals.
*   **Standard Output (stdout/stderr)**: Logs detailing agent activities, review progress, and any errors encountered.