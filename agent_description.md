### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests, automatically analyzing code for typos, grammar errors, code quality issues, and potential security vulnerabilities. Based on its findings, the agent posts detailed comments directly on the pull request or approves it if no issues are detected.

**Key Features:**

*   **Automated Pull Request Review:** Monitors configured GitHub repositories and automatically initiates reviews for new pull requests.
*   **Comprehensive Code Analysis:** Performs checks for:
    *   **Typographical and Grammatical Errors:** Identifies and suggests corrections for text within code, comments, and documentation.
    *   **Code Quality:** Utilizes AI models (OpenAI or Anthropic) to evaluate code against best practices and identify potential issues.
    *   **Security Vulnerabilities:** Detects common security patterns and suggests remediations.
*   **Intelligent Commenting:** Posts inline comments for specific issues and a summary comment for the overall review.
*   **Configurable Behavior:** Allows customization of review types (typos, code quality, security), maximum files/lines to review, and auto-approval for clean PRs.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic large language models for AI-driven analysis.

**Inputs:**

*   **GitHub API:** Fetches pull request details, changed files, and existing comments.
*   **Environment Variables:** Configuration parameters for GitHub authentication, AI provider settings, monitored repositories, and review preferences.
*   **CLI Arguments (stdin):** For manual triggering of a single PR review (repository URL, pull request number).

**Outputs:**

*   **GitHub Pull Request Comments:** Posts detailed inline comments on specific lines of code and a summary comment on the pull request.
*   **GitHub Pull Request Approvals:** Can automatically approve pull requests if no issues are found (if configured).
*   **Console Logs (stdout):** Provides operational status and error messages.

**Configuration:**

The agent's behavior is highly configurable through environment variables, including:

*   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
*   `AI_PROVIDER`: Specifies the AI service (e.g., "openai" or "anthropic").
*   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
*   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., 'owner/repo,owner/repo2') to monitor.
*   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable or disable specific review types.
*   `AUTO_APPROVE_MINOR`: Set to "true" to automatically approve pull requests with no issues.
*   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`: Define the scope of review per pull request and file.
*   `AGENT_NAME`: The name the agent uses in PR comments.
*   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.