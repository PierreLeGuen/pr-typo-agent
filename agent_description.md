### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the pull request review process on GitHub. It monitors specified repositories for new pull requests, performs comprehensive code analysis, and provides detailed feedback directly on GitHub.

#### Main Functions

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Code Review:** Performs detailed analysis of code changes within pull requests.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammatical errors in code and comments.
*   **AI-Powered Code Quality Analysis:** Leverages AI models (OpenAI or Anthropic) to assess code quality, readability, performance, and adherence to best practices.
*   **Security Vulnerability Detection:** Scans for common security issues such as hardcoded secrets, SQL injection risks, and command injection vulnerabilities.
*   **Automated Feedback:** Posts inline comments on specific lines of code with findings and provides a summary comment on the pull request.
*   **Optional Auto-Approval:** Can automatically approve pull requests if no significant issues are detected.
*   **Specific PR Review:** Can be triggered to review a single, specific pull request on demand.

#### Key Features

*   **Configurable Review Types:** Enable or disable typo, code quality, and security reviews independently.
*   **AI Provider Flexibility:** Supports both OpenAI and Anthropic models for AI-driven reviews.
*   **Scalable Review Limits:** Configurable limits on the number of files and lines reviewed per pull request to manage scope and avoid reviewing excessively large changes.
*   **Dry Run Mode:** Allows testing the agent's review capabilities without posting actual comments to GitHub.
*   **Customizable Agent Name:** The name used by the bot when posting comments can be configured.

#### Inputs

*   **Environment Variables (via `.env` file or system environment):**
    *   `GITHUB_TOKEN`: A GitHub Personal Access Token with 'repo' permissions for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service to use for reviews (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`: The API key for the selected AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
    *   `REVIEW_TYPOS`: Boolean flag (`true`/`false`) to enable/disable typo and grammar review.
    *   `REVIEW_CODE_QUALITY`: Boolean flag (`true`/`false`) to enable/disable AI-powered code quality review.
    *   `REVIEW_SECURITY`: Boolean flag (`true`/`false`) to enable/disable security vulnerability review.
    *   `AUTO_APPROVE_MINOR`: Boolean flag (`true`/`false`) to enable/disable automatic PR approval when no issues are found.
    *   `MAX_FILES_PER_REVIEW`: The maximum number of files to review per pull request.
    *   `MAX_LINES_PER_FILE`: The maximum number of lines to review per file.
    *   `AGENT_NAME`: The name the agent uses in PR comments (defaults to "PR Review Bot").
    *   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new pull requests.
    *   `GITHUB_WEBHOOK_SECRET`: An optional secret for validating GitHub webhook payloads.
    *   `MAX_RETRIES`: The maximum number of retries for API calls in case of failures.
*   **Command Line Arguments (for `review` command):**
    *   `repo_url`: The URL of the GitHub repository containing the pull request.
    *   `pr_number`: The specific pull request number to review.

#### Outputs

*   **GitHub Pull Request Comments:**
    *   Inline comments on specific lines of code highlighting findings (e.g., typos, code quality suggestions, security issues).
    *   A comprehensive summary comment posted on the pull request, detailing the review results.
*   **GitHub Pull Request Approvals:** An approval status posted on the pull request if `AUTO_APPROVE_MINOR` is enabled and no issues are found during the review.
*   **Console/Log Output:** Provides detailed logs and status updates during the agent's operation, useful for monitoring and debugging.