## PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It monitors specified repositories for new pull requests and performs comprehensive reviews, providing feedback directly within GitHub.

### Main Functions

*   **Automated Pull Request Review:** Continuously monitors configured GitHub repositories for new pull requests.
*   **Multi-faceted Code Analysis:**
    *   **Typo and Grammar Review:** Identifies and suggests corrections for spelling and grammar errors in new code and comments.
    *   **AI-powered Code Quality Review:** Analyzes code for quality, readability, performance, best practices, and potential bugs using an AI model.
    *   **Security Vulnerability Detection:** Scans for common security issues such as hardcoded secrets, SQL injection risks, and command injection vulnerabilities.
*   **GitHub Integration:** Posts detailed inline comments for specific findings and provides a summary comment on the pull request.
*   **Conditional Approval:** Can be configured to automatically approve pull requests where no issues are detected.
*   **On-Demand Review:** Supports reviewing a specific pull request by providing its repository URL and PR number.
*   **Configurable Behavior:** Allows users to enable/disable specific review types, set limits on files/lines reviewed, and configure polling intervals.

### How it Works

The agent operates by periodically polling the GitHub API for open pull requests in the repositories it is configured to watch. For each new or unreviewed pull request, it fetches the changed files and their content (patches). It then applies various review modules, including AI-powered analysis for code quality and typo correction, and pattern-based checks for security issues. All findings are then formatted and posted as comments directly on the GitHub pull request.

### Inputs

*   **Configuration:** Environment variables (loaded from a `.env` file or system environment) specifying GitHub tokens, AI API keys, watched repositories, and review preferences.
*   **GitHub API:** Fetches pull request data (details, files, comments) from GitHub.
*   **CLI Arguments:** For on-demand review, it accepts a repository URL and pull request number via command-line interface.

### Outputs

*   **GitHub Comments:** Posts inline comments on specific lines of code within a pull request, a summary comment for the entire PR, and optionally an approval comment.
*   **Logs:** Outputs operational logs and review progress to the console/stdout.

### Environment Variables

The agent's behavior is highly configurable through the following environment variables:

*   `GITHUB_TOKEN`: Your GitHub Personal Access Token for API authentication.
*   `AI_PROVIDER`: Specifies the AI service provider ("openai" or "anthropic").
*   `OPENAI_API_KEY`: Your OpenAI API key (if `AI_PROVIDER` is "openai").
*   `ANTHROPIC_API_KEY`: Your Anthropic API key (if `AI_PROVIDER` is "anthropic").
*   `WATCHED_REPOSITORIES`: A comma-separated list of `owner/repo` to monitor.
*   `REVIEW_TYPOS`: Enables/disables typo and grammar review (`true`/`false`).
*   `REVIEW_CODE_QUALITY`: Enables/disables AI-powered code quality review (`true`/`false`).
*   `REVIEW_SECURITY`: Enables/disables security vulnerability review (`true`/`false`).
*   `AUTO_APPROVE_MINOR`: Automatically approves PRs with no issues (`true`/`false`).
*   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
*   `MAX_LINES_PER_FILE`: Maximum lines per file to review.
*   `AGENT_NAME`: The name used when posting comments (e.g., "PR Review Bot").
*   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
*   `MAX_RETRIES`: Maximum retries for API calls.
*   `GITHUB_WEBHOOK_SECRET`: Optional secret for GitHub webhook validation.