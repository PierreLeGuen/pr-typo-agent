# PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It actively monitors specified repositories for new pull requests and performs comprehensive, configurable reviews to identify potential issues before merging.

## Main Functions

*   **Automated Pull Request Monitoring:** Continuously checks a configured list of GitHub repositories for newly opened or updated pull requests.
*   **Intelligent Code Review:** Utilizes AI models (OpenAI or Anthropic) to analyze code for:
    *   **Code Quality:** Identifies best practice violations, readability issues, and potential bugs.
    *   **Security Vulnerabilities:** Detects common security risks like hardcoded secrets, SQL injection, and command injection.
    *   **Typo and Grammar Corrections:** Reviews new or changed lines of code for spelling and grammatical errors.
*   **Automated Feedback:** Posts detailed inline comments directly on the pull request for specific findings and provides a summary comment for the entire review.
*   **Conditional Approval:** Can be configured to automatically approve pull requests where no issues are detected.
*   **On-Demand Review:** Supports reviewing a specific pull request manually via a command-line interface.

## Key Features

*   **Configurable Review Scope:** Users can enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic as AI providers for intelligent analysis.
*   **Customizable Agent Name:** The name displayed in PR comments can be configured.
*   **Dry Run Mode:** Allows testing the agent's review capabilities without posting actual comments to GitHub.

## Inputs

*   **Configuration (Environment Variables):** The agent is configured primarily through environment variables, typically loaded from a `.env` file. These include:
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of `owner/repo` to monitor.
    *   Flags to enable/disable specific review types (`REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`).
    *   Review behavior settings (`AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`).
    *   Agent identification and polling settings (`AGENT_NAME`, `POLLING_INTERVAL`).
*   **Command Line Arguments (stdin):** For on-demand reviews, the agent accepts repository URL and pull request number as arguments.

## Outputs

*   **GitHub Pull Request Comments (HTTP):** The primary output is direct feedback on GitHub pull requests, including:
    *   Inline comments on specific lines of code where issues are found, often with suggestions.
    *   A summary comment at the end of the review, detailing findings or indicating a clean review.
*   **Console Logs (stdout/stderr):** Provides operational logs, status updates, and error messages during execution.