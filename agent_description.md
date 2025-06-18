### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process for GitHub Pull Requests. It monitors specified repositories for new pull requests, applies configurable review checks for code quality, security vulnerabilities, and typos, and then provides feedback directly on the pull request.

#### Key Features

*   **Automated PR Review**: Continuously monitors GitHub repositories for new pull requests or can be invoked to review a specific PR on demand.
*   **AI-Powered Analysis**: Utilizes large language models (from OpenAI or Anthropic) to perform intelligent code quality assessments and detect grammatical errors and typos in code and documentation.
*   **Security Scanning**: Identifies potential security vulnerabilities and common insecure coding patterns within the pull request changes.
*   **Customizable Reviews**: Allows users to enable or disable specific review categories, including typo detection, AI-powered code quality checks, and security analysis.
*   **Automated Approvals**: Can be configured to automatically approve pull requests if no issues are detected during the review process.
*   **Configurable Scope**: Users can set limits on the maximum number of files and lines per file to be reviewed, helping manage the scope of large pull requests.
*   **Detailed Feedback**: Posts inline comments on specific lines of code where issues are found and provides a comprehensive summary comment on the pull request.

#### Inputs

*   **Environment Variables**: Configured via environment variables (or a `.env` file) for authentication, AI provider selection, review settings, and repository monitoring. Examples include `GITHUB_TOKEN`, `AI_PROVIDER`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`, `AGENT_NAME`, `POLLING_INTERVAL`, and `MAX_RETRIES`. (Medium: Environment variables/file system)
*   **GitHub API**: Fetches pull request details, file changes (diffs), and existing comments from monitored repositories. (Medium: HTTP)
*   **Command Line Arguments**: Accepts arguments for specific actions, such as `start` (to begin continuous monitoring) or `review <repo_url> <pr_number>` (to review a single pull request). (Medium: stdin/CLI)

#### Outputs

*   **GitHub Pull Request Comments**: Posts new comments on pull requests, including inline suggestions for specific lines of code and a summary of findings for the entire PR. (Medium: HTTP to GitHub API)
*   **GitHub Pull Request Approvals**: Submits an approval status to a pull request if configured to auto-approve and no issues are found. (Medium: HTTP to GitHub API)
*   **Console/Log Output**: Provides real-time status updates, informational messages, and error logs during its operation. (Medium: stdout/stderr)