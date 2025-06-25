### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new pull requests and performs comprehensive reviews, identifying potential issues before merging.

**Main Functions:**
*   **Automated Pull Request Review**: Continuously checks designated GitHub repositories for new pull requests.
*   **Multi-faceted Code Analysis**: Conducts reviews for:
    *   **Typographical and Grammar Errors**: Utilizes AI (or a simple fallback) to suggest corrections in code comments, documentation, and string literals.
    *   **Code Quality**: Leverages AI models (OpenAI or Anthropic) to provide feedback on code quality, readability, best practices, and potential bugs.
    *   **Security Vulnerabilities**: Scans for common security risks such as hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
*   **Intelligent Commenting**: Posts detailed inline comments directly on the pull request for specific findings, along with a comprehensive summary comment.
*   **Conditional Approval**: Can be configured to automatically approve pull requests if no issues are detected during the review.
*   **Configurable Behavior**: Allows customization of review types, AI provider, file and line limits, and polling intervals.

**Key Features:**
*   Supports OpenAI and Anthropic AI models for intelligent reviews.
*   Can be configured to monitor multiple GitHub repositories.
*   Filters files based on type and size to optimize review scope.
*   Operates in a continuous polling mode or can review a specific PR on demand.
*   Includes a dry-run mode for testing without posting comments.

**Inputs:**
*   **Environment Variables**: Configuration parameters such as GitHub API token, AI provider API keys, watched repositories, and review preferences (`GITHUB_TOKEN`, `AI_PROVIDER`, `OPENAI_API_KEY`/`ANTHROPIC_API_KEY`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`, `AGENT_NAME`, `POLLING_INTERVAL`, `MAX_RETRIES`).
*   **Command Line Arguments**:
    *   `start`: Initiates continuous monitoring based on configured repositories.
    *   `review <repo_url> <pr_number>`: Triggers a review for a specific pull request.

**Outputs:**
*   **GitHub Comments (HTTP)**: Posts inline review comments on specific lines of code and a summary comment on the pull request.
*   **GitHub Pull Request Approvals (HTTP)**: Optionally approves pull requests if no issues are found.
*   **Console Logs (stdout/stderr)**: Provides operational status, review progress, and error messages.