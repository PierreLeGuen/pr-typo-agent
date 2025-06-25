### Agent Name
PR Review Agent

### Summary
The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new or updated pull requests and performs comprehensive reviews, identifying issues related to code quality, security vulnerabilities, and typos. The agent then provides detailed feedback directly on GitHub pull requests, including inline suggestions and a summary of its findings. It can operate in continuous monitoring mode or review a specific pull request on demand.

### Main Functions
*   **Automated Pull Request Monitoring:** Continuously checks a configured list of GitHub repositories for open pull requests.
*   **AI-Powered Code Review:** Utilizes large language models (LLMs) from providers like OpenAI or Anthropic to analyze code changes for:
    *   **Code Quality:** Identifies best practice violations, potential performance issues, and general code improvements.
    *   **Security Vulnerabilities:** Detects common security flaws such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
    *   **Typo and Grammar:** Scans new or changed text for spelling and grammatical errors.
*   **Intelligent Feedback Generation:** Posts detailed review comments directly on GitHub, including:
    *   Inline comments with specific findings and suggested improvements.
    *   A comprehensive summary comment for the entire pull request.
*   **Conditional PR Approval:** Optionally approves pull requests automatically if no issues are detected during the review.
*   **On-Demand Review:** Allows users to trigger a review for a specific pull request by providing its repository URL and PR number.

### Key Features
*   **Configurable Review Types:** Users can enable or disable specific review categories (typos, code quality, security) to tailor the agent's behavior.
*   **Flexible AI Provider:** Supports integration with both OpenAI and Anthropic, allowing users to choose their preferred AI service.
*   **Review Scope Control:** Configurable limits on the maximum number of files and lines reviewed per pull request to manage review complexity and API usage.
*   **Dry Run Mode:** Provides a simulation mode to test the agent's review capabilities without posting actual comments to GitHub.
*   **Interactive Setup:** Includes a command-line utility for an easy, guided configuration process.

### Inputs
*   **Environment Variables:** (Loaded from `.env` file or system environment)
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: Specifies the AI service provider to use (`openai` or `anthropic`).
    *   `OPENAI_API_KEY`: API key for OpenAI (required if `AI_PROVIDER=openai`).
    *   `ANTHROPIC_API_KEY`: API key for Anthropic (required if `AI_PROVIDER=anthropic`).
    *   `WATCHED_REPOSITORIES`: Comma-separated list of `owner/repo` pairs to monitor.
    *   `REVIEW_TYPOS`: Boolean (`true`/`false`) to enable/disable typo review.
    *   `REVIEW_CODE_QUALITY`: Boolean (`true`/`false`) to enable/disable AI code quality review.
    *   `REVIEW_SECURITY`: Boolean (`true`/`false`) to enable/disable security review.
    *   `AUTO_APPROVE_MINOR`: Boolean (`true`/`false`) to enable/disable auto-approval.
    *   `MAX_FILES_PER_REVIEW`: Maximum files to review per PR (integer).
    *   `MAX_LINES_PER_FILE`: Maximum lines to review per file (integer).
    *   `AGENT_NAME`: The name the agent uses in PR comments (e.g., "PR Review Bot").
    *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs (integer).
    *   `MAX_RETRIES`: Maximum retries for API calls (integer).
    *   `GITHUB_WEBHOOK_SECRET`: Optional secret for GitHub webhook validation.
*   **Command Line Arguments (stdin):**
    *   `pr-review-agent start`: Initiates continuous monitoring.
        *   `--config-file <path>`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Enables dry-run mode.
        *   `--verbose`: Enables verbose logging.
    *   `pr-review-agent review <repo_url> <pr_number>`: Reviews a specific pull request.
        *   `<repo_url>`: Full URL of the GitHub repository.
        *   `<pr_number>`: The pull request number.
        *   `--config-file <path>`: Path to the configuration file.
        *   `--dry-run`: Enables dry-run mode.
    *   `pr-review-agent setup`: Interactive setup for configuration, prompting for required keys.

### Outputs
*   **GitHub Pull Request Comments (HTTP):**
    *   Inline comments on specific lines of code within the pull request, highlighting issues and providing suggestions.
    *   A summary comment appended to the pull request, detailing all findings or an approval message.
*   **Console Logs (stdout/stderr):**
    *   Provides real-time status updates on agent operations, including monitoring activities, review progress, and any encountered errors.