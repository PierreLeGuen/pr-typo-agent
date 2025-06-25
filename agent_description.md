### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It monitors specified repositories for new or updated pull requests, performing comprehensive checks on code quality, potential security vulnerabilities, and typos. Based on its findings, the agent posts detailed comments directly on the pull request, providing actionable feedback to developers.

#### Key Features:
*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests, initiating reviews automatically.
*   **AI-Powered Code Analysis:** Leverages advanced AI models (OpenAI or Anthropic) to assess code quality, identify best practice violations, and suggest improvements.
*   **Security Vulnerability Detection:** Scans code for common security issues such as hardcoded secrets, potential SQL injection, and command injection risks.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors within the code and documentation.
*   **Actionable Feedback:** Posts detailed inline comments on specific lines of code where issues are detected, along with a comprehensive summary comment for the entire pull request.
*   **Configurable Review Types:** Allows users to enable or disable specific review categories (typos, code quality, security) based on project requirements.
*   **Automated Approvals:** Can be configured to automatically approve pull requests that pass all configured checks without any detected issues.
*   **Flexible Operation:** Supports both continuous monitoring mode and on-demand review of individual pull requests via command-line interface.

#### Inputs:
*   **GitHub Pull Request Data:** Fetches pull request details, file changes (diffs), and existing comments from GitHub.
    *   **Medium:** HTTP API calls to GitHub.
*   **Configuration:** Environment variables loaded from a `.env` file or directly from the system environment.
    *   **Medium:** File system / Environment.
*   **Command-Line Arguments:** Specific repository URLs, pull request numbers, and operational flags (e.g., dry-run, verbose).
    *   **Medium:** stdin/CLI.
*   **Interactive Setup:** Prompts for GitHub token and AI API keys during initial setup.
    *   **Medium:** stdin/CLI.

#### Outputs:
*   **GitHub Comments:** Posts comments directly on pull requests, including inline suggestions and overall summaries. The agent uses the configurable name "PR Review Bot" by default in its comments.
    *   **Medium:** HTTP API calls to GitHub.
*   **Console Logs:** Provides real-time status updates, errors, and review progress.
    *   **Medium:** stdout.
*   **Configuration File:** Generates or updates a `.env` file during the setup process.
    *   **Medium:** File system.

#### Configuration:
The agent is configured via environment variables. These can be provided directly or loaded from a `.env` file.
*   **`GITHUB_TOKEN`**: (Required) Your GitHub Personal Access Token with `repo` permissions.
*   **`AI_PROVIDER`**: (Required) The AI service provider to use for reviews. Choose "openai" or "anthropic".
*   **`OPENAI_API_KEY`**: (Required if `AI_PROVIDER=openai`) Your OpenAI API key.
*   **`ANTHROPIC_API_KEY`**: (Required if `AI_PROVIDER=anthropic`) Your Anthropic API key.
*   **`WATCHED_REPOSITORIES`**: (Required) A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) that the agent should monitor.
*   **`REVIEW_TYPOS`**: Set to `"true"` to enable typo and grammar review, `"false"` to disable. (Default: `"true"`)
*   **`REVIEW_CODE_QUALITY`**: Set to `"true"` to enable AI-powered code quality review, `"false"` to disable. (Default: `"true"`)
*   **`REVIEW_SECURITY`**: Set to `"true"` to enable security vulnerability review, `"false"` to disable. (Default: `"true"`)
*   **`AUTO_APPROVE_MINOR`**: Set to `"true"` to automatically approve pull requests where no issues are found. (Default: `"false"`)
*   **`MAX_FILES_PER_REVIEW`**: The maximum number of files the agent will review per pull request. (Default: `50`)
*   **`MAX_LINES_PER_FILE`**: The maximum number of lines per file that the agent will review. (Default: `1000`)
*   **`AGENT_NAME`**: The name that the PR Review Agent will use when posting comments on pull requests. (Default: "PR Review Bot")
*   **`POLLING_INTERVAL`**: How often (in seconds) the agent should check for new pull requests when running in monitoring mode. (Default: `300` seconds)
*   **`MAX_RETRIES`**: The maximum number of retries for API calls in case of failures. (Default: `3`)
*   **`GITHUB_WEBHOOK_SECRET`**: (Optional) A secret used for validating GitHub webhook payloads for advanced integrations.