## PR Review Bot

The PR Review Bot is an AI-powered agent designed to automate and enhance the pull request review process on GitHub. It monitors specified repositories for new pull requests and provides comprehensive feedback on code quality, potential security vulnerabilities, and grammatical/spelling errors.

### Main Functions

*   **Automated PR Monitoring & Review:** Continuously watches configured GitHub repositories for new pull requests and automatically initiates reviews.
*   **On-Demand PR Review:** Allows users to trigger a review for a specific pull request by providing its repository URL and PR number.
*   **AI-Powered Code Analysis:** Utilizes large language models (OpenAI or Anthropic) to assess code quality, identify best practice violations, and suggest improvements.
*   **Typo and Grammar Detection:** Scans new code additions for spelling and grammatical errors, providing inline suggestions.
*   **Security Vulnerability Scanning:** Detects common security risks such as hardcoded secrets, potential SQL injection, command injection, and usage of weak cryptographic algorithms.
*   **Automated Feedback:** Posts detailed inline comments on specific lines of code where issues are found, and provides a comprehensive summary comment on the pull request.
*   **Conditional PR Approval:** Can be configured to automatically approve pull requests that pass all configured checks without any issues.
*   **Interactive Setup:** Provides a command-line utility to guide users through the initial configuration process.

### Important Details

*   **Customizable Reviews:** Users can enable or disable specific review types (typos, code quality, security) based on their needs.
*   **Configurable Scope:** Allows setting limits on the maximum number of files and lines reviewed per pull request to manage review scope and AI token usage.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic API services for AI-driven analysis.
*   **GitHub Integration:** Authenticates using a GitHub Personal Access Token to interact with repositories.
*   **Polling-Based Operation:** Operates by periodically polling GitHub for new pull requests in watched repositories.

### Inputs

*   **Environment Variables (via `.env` file or system environment):**
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for authentication.
    *   `AI_PROVIDER`: Choice of AI service (`openai` or `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag for auto-approval.
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Integers for review scope limits.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor.
    *   `AGENT_NAME`: Name used in PR comments.
    *   `POLLING_INTERVAL`: Frequency (in seconds) for checking new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
*   **Command Line Arguments (stdin/CLI):**
    *   `repo_url`: URL of the repository for specific PR review.
    *   `pr_number`: Pull request number for specific PR review.
    *   `config_file`: Path to the configuration file.
    *   `dry_run`: Flag to run in dry-run mode without posting comments.
    *   `verbose`: Flag to enable verbose logging.
    *   Interactive prompts during `setup` command for API keys and provider.
*   **GitHub API (Polling):** Information about open pull requests and their files.

### Outputs

*   **GitHub Comments (HTTP/API):**
    *   Inline comments on specific lines of code with findings and suggestions.
    *   Overall summary comments on the pull request.
    *   Approval comments when no issues are found and auto-approval is enabled.
*   **Console Output (stdout):**
    *   Operational logs, status updates, and error messages.
    *   Confirmation messages during setup and command execution.
*   **Configuration File (filesystem):**
    *   A `.env` file generated during the interactive setup process.