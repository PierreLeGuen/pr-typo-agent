### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It monitors specified repositories for new pull requests and provides comprehensive feedback on code quality, potential security vulnerabilities, and grammatical/spelling errors.

#### Key Features

*   **Automated Code Review:** Leverages AI (OpenAI or Anthropic) to analyze code changes for best practices, performance issues, and potential bugs.
*   **Security Scanning:** Identifies common security vulnerabilities such as hardcoded secrets, SQL injection risks, and command injection patterns.
*   **Typo and Grammar Check:** Reviews new or modified text for spelling and grammatical errors, offering suggestions for correction.
*   **Configurable Reviews:** Allows users to enable or disable specific review types (typos, code quality, security) based on their needs.
*   **Flexible Operation:** Can operate in a continuous polling mode to monitor multiple repositories or be triggered to review a specific pull request on demand.
*   **Detailed Feedback:** Posts inline comments on GitHub for specific findings and provides a summary comment on the pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests if no issues are detected.
*   **Scope Management:** Limits the number of files and lines reviewed per pull request to manage review scope and AI token usage.

#### Inputs

The agent's behavior is primarily configured through environment variables or a `.env` file. It can also accept command-line arguments for specific operations.

*   **Environment Variables:**
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Specifies the AI service (e.g., "openai", "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API keys for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Set to `true` to automatically approve PRs with no issues.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Limits for the review scope.
    *   `AGENT_NAME`: The name the bot uses in PR comments (defaults to "PR Review Bot").
    *   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for webhook validation.
    *   `MAX_RETRIES`: Maximum retries for API calls.
*   **Command Line Arguments:**
    *   `start`: Initiates continuous monitoring. Accepts `config_file`, `dry_run`, and `verbose` options.
    *   `review <repo_url> <pr_number>`: Reviews a specific pull request. Accepts `config_file` and `dry_run` options.
    *   `setup`: An interactive command to help generate a basic `.env` configuration file.

#### Outputs

The agent communicates its findings directly on GitHub pull requests.

*   **GitHub Pull Request Comments:**
    *   **Inline Comments:** Posts specific findings (typos, code quality issues, security concerns) as comments on the relevant lines of code.
    *   **Summary Comment:** Adds a comprehensive summary of the review at the end of the pull request, detailing the types and counts of issues found, or an approval message if no issues are detected.
*   **Console/Log Output:** Provides status updates, debug information, and error messages to the standard output.