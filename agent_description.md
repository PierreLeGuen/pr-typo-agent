### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories or can be invoked to review a single PR, providing automated feedback on various aspects of the code.

#### Features

*   **Automated Code Review**: Automatically reviews pull requests for a range of issues.
*   **Typo and Grammar Detection**: Identifies and suggests corrections for spelling and grammar errors in code comments, documentation, and string literals, leveraging AI for improved accuracy.
*   **AI-Powered Code Quality Analysis**: Utilizes large language models (LLMs) to assess code quality, readability, best practices, and potential bugs.
*   **Security Vulnerability Detection**: Scans for common security patterns such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **Configurable Review Scope**: Allows setting limits on the maximum number of files and lines reviewed per pull request to manage processing load.
*   **GitHub Integration**: Posts detailed inline comments directly on the relevant lines of code and provides a comprehensive summary comment on the pull request.
*   **AI Provider Flexibility**: Supports both OpenAI and Anthropic as AI backend providers for intelligent review capabilities.
*   **Continuous Monitoring**: Can be configured to poll GitHub repositories at a specified interval for new pull requests.
*   **On-Demand Review**: Provides a command-line interface to review a specific pull request instantly.
*   **Dry Run Mode**: Allows testing the agent's review capabilities without actually posting comments to GitHub.
*   **Customizable Agent Name**: The name displayed in PR comments can be configured.
*   **Optional Auto-Approval**: Can be set to automatically approve pull requests if no issues are found during the review.

#### Inputs

*   **Configuration**:
    *   **Medium**: Environment variables loaded from a `.env` file.
    *   **Details**:
        *   `GITHUB_TOKEN`: A GitHub Personal Access Token with repository permissions.
        *   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
        *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
        *   `REVIEW_TYPOS`: Enables/disables typo review.
        *   `REVIEW_CODE_QUALITY`: Enables/disables AI code quality review.
        *   `REVIEW_SECURITY`: Enables/disables security review.
        *   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
        *   `AGENT_NAME`: The name used for comments.
        *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
        *   `MAX_FILES_PER_REVIEW`: Maximum files to review per PR.
        *   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
        *   `AUTO_APPROVE_MINOR`: Enables/disables auto-approval.
*   **GitHub Pull Requests**:
    *   **Medium**: GitHub API.
    *   **Details**: Pull request details, changed files, and diffs from monitored repositories.
*   **Command Line Arguments**:
    *   **Medium**: `stdin` (command line).
    *   **Details**: Repository URL and pull request number when using the `review` command.

#### Outputs

*   **GitHub Comments**:
    *   **Medium**: GitHub API.
    *   **Details**:
        *   Inline comments on specific lines of code detailing findings (typos, code quality suggestions, security warnings).
        *   A summary comment on the pull request, indicating the types and counts of issues found or an approval message if no issues are detected.
*   **Console Output**:
    *   **Medium**: `stdout`.
    *   **Details**: Logs status messages, errors, and dry-run information for operational monitoring.