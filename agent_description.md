### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate code reviews on GitHub pull requests. It continuously monitors specified repositories, applying configurable AI and pattern-based checks for code quality, security vulnerabilities, and typos. Based on its findings, it posts detailed review comments or automatically approves pull requests.

#### Functions

*   **Automated Pull Request Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Configurable Code Review**: Performs comprehensive reviews based on enabled categories:
    *   **Code Quality**: Utilizes AI to assess code quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Detection**: Identifies potential security issues such as hardcoded secrets, SQL injection risks, and command injection.
    *   **Typo and Grammar Checking**: Reviews new lines of code and comments for spelling and grammar errors, optionally using AI for corrections.
*   **Automated Feedback**: Posts detailed inline comments on pull requests for specific issues and provides a comprehensive summary comment.
*   **Conditional PR Approval**: Can be configured to automatically approve pull requests if no issues are detected.
*   **On-Demand Review**: Supports reviewing a single, specific pull request by providing its repository URL and PR number.

#### Inputs

*   **Environment Variables**: Configuration is provided through environment variables, including:
    *   GitHub authentication token (`GITHUB_TOKEN`).
    *   AI provider selection (OpenAI or Anthropic) and API keys (`AI_PROVIDER`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).
    *   Review preferences (e.g., `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AUTO_APPROVE_MINOR`).
    *   Review scope limits (e.g., `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`).
    *   List of GitHub repositories to monitor (`WATCHED_REPOSITORIES`).
    *   Agent identity (`AGENT_NAME`) and operational parameters (`POLLING_INTERVAL`, `MAX_RETRIES`).
*   **GitHub API**: Receives pull request details, changed files, and existing comments directly from the GitHub API.
*   **Command Line Arguments**: For on-demand reviews, the agent accepts a repository URL and pull request number via command-line.

#### Outputs

*   **GitHub Pull Request Comments**: Posts detailed inline comments on specific lines of code where issues (typos, code quality, security) are identified.
*   **GitHub Pull Request Summary**: Adds a summary comment to the pull request, outlining detected issues or an approval message if no issues are found.
*   **GitHub Pull Request Approvals**: Optionally approves pull requests on GitHub if no issues are detected based on configuration.
*   **Console Output**: Provides logging information about its operations and status.