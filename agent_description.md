## PR Review Agent

An AI-powered agent for automated code review and typo detection on GitHub pull requests. It monitors specified repositories for new pull requests, reviews code quality, security, and typos, and posts comments or approvals based on its findings.

### Key Features

*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for new pull requests.
*   **Comprehensive Code Review**:
    *   **AI-Powered Code Quality**: Utilizes OpenAI or Anthropic to assess code quality, identify best practice violations, and suggest improvements.
    *   **Security Vulnerability Detection**: Scans for common security issues like hardcoded secrets, SQL injection risks, and weak cryptographic algorithms.
    *   **Typo and Grammar Correction**: Identifies and suggests corrections for spelling and grammar errors in code and documentation.
*   **Intelligent Feedback**: Posts detailed inline comments on specific lines of code where issues are found, along with a summary comment on the pull request.
*   **Conditional Approval**: Can be configured to automatically approve pull requests if no issues are detected.
*   **Configurable Behavior**: Allows customization of review types, file/line limits, polling intervals, and the AI provider used.
*   **On-Demand Review**: Supports reviewing a specific pull request manually via a command-line interface.

### Inputs

*   **Environment Variables**: Configured via environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, `AGENT_NAME`, etc.) loaded from a `.env` file or directly from the environment.
*   **CLI Arguments**:
    *   `start`: Optional `config_file`, `dry_run` flag, `verbose` flag.
    *   `review`: Required `repo_url` and `pr_number`, optional `config_file`, `dry_run` flag.
    *   `setup`: Interactive prompts for `GITHUB_TOKEN`, `AI_PROVIDER`, and AI API keys (stdin).
*   **GitHub API**: Pull Request data, including files, diffs, and existing comments.

### Outputs

*   **GitHub Comments**: Posts detailed inline comments on specific lines within a pull request and a summary comment on the overall pull request (via GitHub API).
*   **GitHub Approvals**: Posts an approval comment on pull requests if configured and no issues are found (via GitHub API).
*   **Logs**: Outputs operational logs and status messages to stdout.