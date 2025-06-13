### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests and performs comprehensive, configurable reviews, providing detailed feedback directly on GitHub.

#### Key Features

*   **Automated Pull Request Monitoring:** Periodically checks configured GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Review:**
    *   **Typo and Grammar Checking:** Identifies and suggests corrections for spelling and grammar errors in new or modified code lines. Can leverage an AI model for advanced corrections.
    *   **AI-Powered Code Quality Review:** Utilizes large language models (OpenAI or Anthropic) to assess code quality, identify potential bugs, and suggest best practice improvements.
    *   **Security Vulnerability Detection:** Scans for common security issues such as hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
*   **Configurable Review Scope:** Allows setting limits on the maximum number of files and lines of code reviewed per pull request to manage review load.
*   **Intelligent Feedback:** Posts detailed inline comments for specific findings and a comprehensive summary comment for the entire review on the pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic as AI service providers for its advanced review capabilities.
*   **Dry-Run Mode:** Allows users to test the agent's review logic without posting actual comments to GitHub.
*   **On-Demand Review:** Can be triggered to review a specific pull request by its repository URL and pull request number.

#### Inputs

*   **Environment Variables:** The agent's behavior and credentials are configured through environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, etc.). These are typically loaded from a `.env` file.
*   **GitHub API (Polling):** The agent polls the GitHub API to discover new open pull requests in the configured repositories.
*   **Command Line Arguments (stdin):** For on-demand reviews, the agent accepts a repository URL and pull request number as command-line arguments.

#### Outputs

*   **GitHub Comments:** Posts detailed comments on pull requests, including inline suggestions for specific lines of code and a summary of all identified findings.
*   **GitHub Approvals:** If configured, the agent can approve pull requests where no issues are found.
*   **Console/Log Output (stdout):** Provides operational logs, status updates, and error messages to the console.

#### Configuration

The agent is highly configurable via the following environment variables:

*   **`GITHUB_TOKEN`**: A GitHub Personal Access Token with `repo` permissions for API authentication.
*   **`GITHUB_WEBHOOK_SECRET`**: (Optional) A secret for validating GitHub webhook payloads.
*   **`AI_PROVIDER`**: Specifies the AI service (e.g., "openai", "anthropic").
*   **`OPENAI_API_KEY`**: Required if `AI_PROVIDER` is "openai".
*   **`ANTHROPIC_API_KEY`**: Required if `AI_PROVIDER` is "anthropic".
*   **`REVIEW_TYPOS`**: Enables/disables typo and grammar review (`true`/`false`).
*   **`REVIEW_CODE_QUALITY`**: Enables/disables AI-powered code quality review (`true`/`false`).
*   **`REVIEW_SECURITY`**: Enables/disables security vulnerability review (`true`/`false`).
*   **`AUTO_APPROVE_MINOR`**: Enables/disables automatic approval for PRs with no issues (`true`/`false`).
*   **`MAX_FILES_PER_REVIEW`**: Maximum number of files to review per PR.
*   **`MAX_LINES_PER_FILE`**: Maximum number of lines per file to review.
*   **`WATCHED_REPOSITORIES`**: Comma-separated list of `owner/repo` to monitor.
*   **`AGENT_NAME`**: The name the agent uses in PR comments.
*   **`POLLING_INTERVAL`**: How often (in seconds) to check for new PRs.
*   **`MAX_RETRIES`**: Maximum retries for API calls.