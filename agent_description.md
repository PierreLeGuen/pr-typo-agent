### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the pull request review process on GitHub. It monitors specified repositories for new pull requests and performs comprehensive code reviews, posting findings directly as comments on the PRs.

**Main Functions:**

*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Review:** Conducts various types of reviews, including:
    *   **Typo and Grammar Detection:** Identifies spelling and grammatical errors in added lines of code and comments, offering suggestions. This can leverage an AI model or a simple rule-based checker.
    *   **AI-powered Code Quality Review:** Utilizes large language models (LLMs) from OpenAI or Anthropic to assess code quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Detection:** Scans for common security risks such as hardcoded secrets, potential SQL injection, command injection, and weak cryptographic algorithms.
*   **GitHub Integration:** Posts detailed inline comments for specific findings and a comprehensive summary comment on the pull request.
*   **Configurable Behavior:** Allows users to customize review types, maximum file/line limits, polling intervals, and an option to auto-approve PRs with no issues.
*   **On-Demand Review:** Supports reviewing a specific pull request by providing its repository URL and PR number.
*   **Interactive Setup:** Provides a command-line utility to guide users through initial configuration.

**Inputs:**

*   **Configuration (Environment Variables):** Loaded from a `.env` file or environment variables, including:
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API access.
    *   `AI_PROVIDER`: Choice of AI service (`openai` or `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor.
    *   Flags to enable/disable specific review types (`REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`).
    *   `MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`, `POLLING_INTERVAL`, `AGENT_NAME`, etc.
*   **GitHub Pull Request Data:** Fetched directly from the GitHub API (via HTTP).
*   **Command-line Arguments:**
    *   `start`: Initiates continuous monitoring.
    *   `review <repo_url> <pr_number>`: Triggers a review for a specific PR.
    *   `setup`: Guides interactive configuration.

**Outputs:**

*   **GitHub Pull Request Comments (HTTP):**
    *   Inline comments on specific lines of code with detailed findings and suggestions.
    *   Summary comments on the main PR thread, summarizing all detected issues or indicating approval.
*   **Console Output (stdout):** Status messages, errors, and informational logs during operation.