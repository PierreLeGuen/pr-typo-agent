### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new pull requests and performs comprehensive reviews, identifying potential issues related to code quality, security vulnerabilities, and typos. The agent provides detailed feedback directly on GitHub pull requests, helping maintain high code standards and streamline development workflows.

#### Key Features

*   **Automated Pull Request Monitoring:** Continuously checks designated GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review:** Utilizes large language models (OpenAI or Anthropic) to analyze code for quality, best practices, and potential bugs.
*   **Security Vulnerability Detection:** Scans code for common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors in code comments, documentation, and string literals.
*   **Configurable Review Scope:** Allows users to enable or disable specific review types (typos, code quality, security) based on project needs.
*   **Intelligent Commenting:** Posts detailed inline comments on specific lines of code where issues are found, along with a comprehensive summary comment for the entire pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests that pass all configured checks without any detected issues.
*   **Review Limits:** Configurable limits on the number of files and lines per file to review, helping manage API usage and focus on relevant changes.

#### Inputs

The agent is configured primarily through environment variables, which can be loaded from a `.env` file. It also accepts command-line arguments for specific actions.

*   **Environment Variables (Configuration):**
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: The AI service provider to use ("openai" or "anthropic").
    *   `OPENAI_API_KEY`: Your OpenAI API key (if `AI_PROVIDER` is "openai").
    *   `ANTHROPIC_API_KEY`: Your Anthropic API key (if `AI_PROVIDER` is "anthropic").
    *   `WATCHED_REPOSITORIES`: A comma-separated list of `owner/repo` pairs to monitor.
    *   `REVIEW_TYPOS`: `true` or `false` to enable/disable typo review.
    *   `REVIEW_CODE_QUALITY`: `true` or `false` to enable/disable AI code quality review.
    *   `REVIEW_SECURITY`: `true` or `false` to enable/disable security review.
    *   `AUTO_APPROVE_MINOR`: `true` or `false` to enable/disable auto-approval for clean PRs.
    *   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum number of lines per file to review.
    *   `AGENT_NAME`: The name the agent uses in its GitHub comments (e.g., "PR Review Bot").
    *   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for GitHub webhook validation.

*   **Command Line Arguments:**
    *   **`pr-review-agent start`**: Initiates continuous monitoring of `WATCHED_REPOSITORIES`.
        *   `--config-file`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Runs the review without posting comments to GitHub.
        *   `--verbose`: Enables detailed logging.
    *   **`pr-review-agent review <repo_url> <pr_number>`**: Reviews a specific pull request once.
        *   `<repo_url>`: The full URL of the GitHub repository.
        *   `<pr_number>`: The pull request number.
        *   `--config-file`: Path to the configuration file.
        *   `--dry-run`: Runs the review without posting comments to GitHub.
    *   **`pr-review-agent setup`**: Provides an interactive prompt to generate a basic `.env` configuration file.

#### Outputs

*   **GitHub Comments (via HTTP):**
    *   **Inline Comments:** Posted directly on specific lines within pull request files, detailing findings (typos, code quality issues, security concerns) and often including suggested fixes.
    *   **Summary Comments:** A general comment posted on the pull request providing an overview of the review, including a count of issues found by type.
    *   **Approval Comments:** If `AUTO_APPROVE_MINOR` is enabled and no issues are found, the agent will post a celebratory approval comment.
*   **Console/Log Output (stdout/stderr):** Provides real-time status updates, warnings, and error messages during operation.