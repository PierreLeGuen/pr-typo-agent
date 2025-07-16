### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process for GitHub pull requests. It continuously monitors specified repositories for new or updated pull requests, performing a detailed analysis of code changes for quality, security vulnerabilities, and typos. Based on its findings, the agent provides actionable feedback directly on the pull request, streamlining development workflows.

#### Key Features

*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Comprehensive Code Review**:
    *   **Code Quality**: Utilizes advanced AI models (OpenAI or Anthropic) to identify best practices violations, performance issues, and potential bugs.
    *   **Security Analysis**: Scans for common security vulnerabilities such as hardcoded secrets, SQL injection risks, and command injection.
    *   **Typo and Grammar Check**: Reviews new code and comments for spelling and grammar errors, offering suggestions for correction.
*   **Direct GitHub Feedback**: Posts detailed inline comments on specific lines of code where issues are found, along with a summary comment for the entire review.
*   **Configurable Review Types**: Allows users to enable or disable typo, code quality, and security reviews independently.
*   **Smart Approval**: Can be configured to automatically approve pull requests if no issues are detected.
*   **Customizable Scope**: Users can set limits on the maximum number of files and lines reviewed per pull request.
*   **Flexible AI Integration**: Supports both OpenAI and Anthropic API services for AI-driven reviews.
*   **On-demand Review**: Can be triggered to review a specific pull request manually via a command-line interface.

#### Inputs

*   **Configuration (Environment Variables)**:
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
    *   `OPENAI_API_KEY`: Required if `AI_PROVIDER` is "openai".
    *   `ANTHROPIC_API_KEY`: Required if `AI_PROVIDER` is "anthropic".
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`: Enables/disables typo review (`true`/`false`).
    *   `REVIEW_CODE_QUALITY`: Enables/disables AI code quality review (`true`/`false`).
    *   `REVIEW_SECURITY`: Enables/disables security review (`true`/`false`).
    *   `AUTO_APPROVE_MINOR`: Enables/disables automatic approval for PRs with no issues (`true`/`false`).
    *   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum number of lines to review per file.
    *   `AGENT_NAME`: The name used when posting comments (defaults to "PR Review Bot").
    *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
*   **GitHub Pull Request Data (HTTP/API)**: The agent fetches pull request details, changed files, and patch content directly from the GitHub API.
*   **Command Line Arguments (stdin)**: For on-demand reviews, the agent accepts a repository URL and pull request number.

#### Outputs

*   **GitHub Comments (HTTP/API)**: Posts new comments on pull requests, including inline suggestions for specific code lines and a general summary of findings or an approval message.
*   **Console Output (stdout)**: Provides logs and status updates during operation.