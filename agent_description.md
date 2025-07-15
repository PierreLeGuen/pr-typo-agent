### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new or updated pull requests, performing comprehensive reviews for various aspects of code quality, security, and content.

#### Main Functions

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for open pull requests.
*   **Intelligent Code Review:** Utilizes AI models (OpenAI or Anthropic) to review code changes for:
    *   **Code Quality:** Identifies best practice violations, potential bugs, and readability issues.
    *   **Security Vulnerabilities:** Detects common security flaws like hardcoded secrets, SQL injection risks, and command injection.
    *   **Typo and Grammar:** Reviews new or changed text for spelling and grammatical errors.
*   **Contextual Feedback:** Posts detailed review comments directly on the pull request, including inline comments on specific lines of code where issues are found.
*   **Review Summaries:** Provides a comprehensive summary of all findings at the end of each review.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **On-Demand Review:** Allows for a specific pull request to be reviewed manually via a command-line interface.

#### Key Features

*   **Configurable Review Scope:** Users can enable or disable specific review types (typos, code quality, security).
*   **Resource Management:** Limits the number of files and lines reviewed per pull request to manage API usage and review time.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic as AI providers.
*   **Customizable Agent Name:** The name displayed in PR comments can be configured.
*   **Polling-Based Operation:** Operates by periodically polling GitHub for new PRs.

#### Inputs

*   **Environment Variables:**
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for authentication.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` to monitor.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable auto-approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Numerical limits for review scope.
    *   `AGENT_NAME`: The display name for the bot in PR comments.
    *   `POLLING_INTERVAL`: Frequency (in seconds) for checking new PRs.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
    *   `MAX_RETRIES`: Maximum retries for API calls.
*   **Command Line (for specific PR review):**
    *   `repo_url`: The URL of the GitHub repository.
    *   `pr_number`: The pull request number.

#### Outputs

*   **GitHub Pull Request Comments (HTTP):**
    *   Inline comments on specific lines of code, highlighting issues with descriptions and suggestions.
    *   A main summary comment on the pull request, detailing the review findings or indicating approval.
*   **Standard Output (stdout):**
    *   Logs and status messages indicating agent activity, review progress, and any errors.