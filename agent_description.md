### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new or updated pull requests and provides comprehensive feedback directly on GitHub.

#### Key Features
*   **Automated Code Review**: Automatically reviews pull requests for various issues, including:
    *   **Typo and Grammar Checks**: Identifies and suggests corrections for spelling and grammar errors in code comments, documentation, and added code lines.
    *   **AI-Powered Code Quality Analysis**: Utilizes AI models (OpenAI or Anthropic) to assess code quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Detection**: Scans for common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **Configurable Review Scope**: Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **Flexible Operation**: Can operate in a continuous monitoring mode, periodically checking for new PRs, or be triggered to review a specific pull request on demand.
*   **GitHub Integration**: Posts detailed findings as inline comments on specific lines of code and provides a summary comment on the pull request.
*   **Automated Approval**: Optionally approves pull requests if no issues are detected during the review.
*   **Customizable Agent Name**: The name used by the agent when posting comments is configurable.

#### Configuration
The agent is configured primarily through environment variables, which can be loaded from a `.env` file. Key configurations include:
*   **GitHub Token**: A Personal Access Token with repository permissions for interacting with the GitHub API.
*   **AI Provider**: Choice between OpenAI and Anthropic for AI-driven reviews, along with the corresponding API key.
*   **Watched Repositories**: A comma-separated list of `owner/repo` pairs to monitor.
*   **Review Settings**: Flags to enable/disable typo, code quality, and security reviews.
*   **Behavior Settings**: Controls for auto-approval, maximum files/lines per review, polling interval, and API retry limits.

#### Inputs
*   **Environment Variables**: Configured via `.env` file or system environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `OPENAI_API_KEY`).
*   **Command Line Arguments**:
    *   `start`: Initiates continuous monitoring of configured repositories.
    *   `review <repo_url> <pr_number>`: Triggers a review for a specific pull request.
    *   `setup`: Provides an interactive prompt to generate a basic `.env` configuration file.
*   **GitHub Pull Requests**: The agent processes the code changes within open pull requests in the watched repositories.

#### Outputs
*   **GitHub Comments**: The agent posts comments on pull requests, including:
    *   Inline comments on specific lines of code where issues are found (e.g., typos, code quality suggestions, security warnings).
    *   A summary comment on the pull request, detailing the types and counts of issues found or indicating a clean review.
*   **GitHub Approvals**: If `AUTO_APPROVE_MINOR` is enabled and no issues are found, the agent may post an approval.
*   **Console Logs**: Provides detailed logging of its operations, including monitoring status, review progress, and any errors encountered.