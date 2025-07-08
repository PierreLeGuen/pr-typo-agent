### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests, applying intelligent analysis to identify potential issues before they are merged.

**Main Functions:**

*   **Automated Code Review**: Analyzes pull requests for code quality, adherence to best practices, and potential performance issues using a configurable AI provider (OpenAI or Anthropic).
*   **Security Vulnerability Detection**: Scans code changes for common security risks such as hardcoded secrets, SQL injection vulnerabilities, and weak cryptographic algorithms.
*   **Typo and Grammar Checking**: Reviews added or modified text within code and documentation for spelling and grammar errors, offering suggestions for correction.
*   **Intelligent Commenting**: Posts detailed inline comments on specific lines of code where issues are detected, and provides a comprehensive summary comment on the pull request.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests where no significant issues are found, streamlining the review workflow for minor changes.
*   **Repository Monitoring**: Monitors a configurable list of GitHub repositories, automatically initiating reviews for new pull requests.

**Inputs:**

*   **Configuration**: Environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `OPENAI_API_KEY`/`ANTHROPIC_API_KEY`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`, `POLLING_INTERVAL`, `AGENT_NAME`). These are typically loaded from a `.env` file.
*   **GitHub Pull Requests**: The agent retrieves pull request details, including file changes and patch content, directly from the GitHub API.
*   **Command Line Arguments (for manual review)**:
    *   `repo_url`: The URL of the GitHub repository (e.g., `https://github.com/owner/repo`).
    *   `pr_number`: The specific pull request number to review.

**Outputs:**

*   **GitHub Comments**: Posts review comments directly onto the pull request interface, including:
    *   Inline comments on specific lines of code with identified issues, suggestions, and relevant emojis.
    *   A summary comment on the pull request detailing the types and counts of issues found.
*   **GitHub Approvals**: If configured and no issues are found, the agent will post an approval comment on the pull request.
*   **Logs**: Provides detailed operational logs to standard output, indicating its activities, findings, and any errors encountered.