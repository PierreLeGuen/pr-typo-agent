### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new or updated pull requests, performing comprehensive checks for code quality, potential security vulnerabilities, and grammatical or spelling errors. Upon identifying issues, the agent posts detailed feedback directly on the pull request, including inline comments for specific lines of code and an overall summary. It can also be configured to automatically approve pull requests that pass all checks without issues.

#### Key Features

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Quality Review:** Utilizes large language models (OpenAI or Anthropic) to assess code quality, adherence to best practices, and potential bugs.
*   **Security Vulnerability Detection:** Identifies common security issues such as hardcoded secrets, SQL injection risks, and command injection vulnerabilities.
*   **Typo and Grammar Correction:** Reviews code comments, documentation, and string literals for spelling and grammar errors, providing suggested corrections.
*   **Detailed Feedback:** Posts inline comments on specific lines of code where issues are found and provides a comprehensive summary comment on the pull request.
*   **Configurable Review Types:** Allows users to enable or disable specific review categories (typos, code quality, security) based on their needs.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests that pass all enabled checks without any detected issues.
*   **Scalable Review Limits:** Supports configuration for maximum files and lines per file to review, preventing the agent from being overwhelmed by very large pull requests.
*   **Flexible Operation:** Can operate in a continuous polling mode for ongoing monitoring or be triggered to review a specific pull request on demand.

#### Inputs

*   **GitHub API (HTTP):** Receives pull request data, file changes (diffs), and existing comments from monitored repositories.
*   **Environment Variables:** Configuration settings for GitHub authentication, AI provider API keys, watched repositories, review preferences, and operational parameters.
*   **Command Line Arguments (stdin):** For `review` command, takes a repository URL and PR number.

#### Outputs

*   **GitHub API (HTTP):**
    *   Posts inline review comments on specific lines of code.
    *   Posts summary comments on the pull request.
    *   Submits pull request approvals if the `AUTO_APPROVE_MINOR` setting is enabled and no issues are found.
*   **Console/Logs (stdout):** Provides operational logs, status updates, and error messages during execution.

#### Configuration

The agent's behavior is controlled by the following environment variables:

*   **`GITHUB_TOKEN`**: Your GitHub Personal Access Token with `repo` permissions.
*   **`AI_PROVIDER`**: The AI service provider to use for reviews (e.g., `openai`, `anthropic`).
*   **`OPENAI_API_KEY`**: Your OpenAI API key (required if `AI_PROVIDER` is `openai`).
*   **`ANTHROPIC_API_KEY`**: Your Anthropic API key (required if `AI_PROVIDER` is `anthropic`).
*   **`WATCHED_REPOSITORIES`**: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
*   **`REVIEW_TYPOS`**: Set to `true` to enable typo and grammar review, `false` to disable.
*   **`REVIEW_CODE_QUALITY`**: Set to `true` to enable AI-powered code quality review, `false` to disable.
*   **`REVIEW_SECURITY`**: Set to `true` to enable security vulnerability review, `false` to disable.
*   **`AUTO_APPROVE_MINOR`**: Set to `true` to automatically approve pull requests where no issues are found.
*   **`MAX_FILES_PER_REVIEW`**: The maximum number of files the agent will review per pull request.
*   **`MAX_LINES_PER_FILE`**: The maximum number of lines per file that the agent will review.
*   **`AGENT_NAME`**: The name that the agent will use when posting comments on pull requests (defaults to "PR Review Bot").
*   **`POLLING_INTERVAL`**: How often (in seconds) the agent should check for new pull requests.
*   **`GITHUB_WEBHOOK_SECRET`**: An optional secret used for validating GitHub webhook payloads for advanced integrations.
*   **`MAX_RETRIES`**: The maximum number of retries for API calls in case of failures.