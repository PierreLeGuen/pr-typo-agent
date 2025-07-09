### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests, performs comprehensive reviews, and provides actionable feedback directly within GitHub.

#### Key Features

*   **Automated Code Review**: Automatically reviews pull requests for various aspects including:
    *   **Typo and Grammar Detection**: Identifies and suggests corrections for spelling and grammar errors in code and documentation.
    *   **AI-Powered Code Quality Analysis**: Utilizes AI models (OpenAI or Anthropic) to assess code quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Detection**: Scans for common security issues such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **Configurable Review Scope**: Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **Intelligent Feedback**: Posts detailed inline comments on specific lines of code where issues are found, along with suggested improvements.
*   **Comprehensive Summaries**: Provides a summary comment on the pull request, listing all detected issues by type.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Flexible Operation**: Can operate in a continuous polling mode to monitor repositories or be triggered to review a specific pull request on demand.
*   **Dry Run Mode**: Supports a dry-run mode to simulate reviews without posting actual comments to GitHub.

#### Inputs

*   **Environment Variables**:
    *   `GITHUB_TOKEN`: A GitHub Personal Access Token with `repo` permissions for API authentication.
    *   `AI_PROVIDER`: The AI service provider (e.g., "openai" or "anthropic").
    *   `OPENAI_API_KEY`: API key for OpenAI (if `AI_PROVIDER` is "openai").
    *   `ANTHROPIC_API_KEY`: API key for Anthropic (if `AI_PROVIDER` is "anthropic").
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`: (boolean) Enables/disables typo review.
    *   `REVIEW_CODE_QUALITY`: (boolean) Enables/disables AI code quality review.
    *   `REVIEW_SECURITY`: (boolean) Enables/disables security review.
    *   `AUTO_APPROVE_MINOR`: (boolean) Enables/disables automatic approval for PRs with no issues.
    *   `MAX_FILES_PER_REVIEW`: Maximum files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
    *   `AGENT_NAME`: The name used for comments posted by the agent.
    *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: (Optional) Secret for GitHub webhook validation.
*   **GitHub API (HTTP)**: Pull request data (files, diffs, existing comments) from monitored repositories.
*   **Command Line Arguments**: For on-demand review, `repo_url` and `pr_number`.

#### Outputs

*   **GitHub API (HTTP)**:
    *   Inline review comments on specific lines of code within a pull request.
    *   Summary comments posted on the pull request.
    *   Pull request approvals (if `AUTO_APPROVE_MINOR` is enabled and no issues are found).
*   **Standard Output/Error (stdout/stderr)**: Logging information about agent activities, errors, and status updates.