### Agent Name
PR Review Agent (also known as "PR Review Bot" in comments)

### Summary
The PR Review Agent is an AI-powered tool designed to automate code review processes on GitHub pull requests. It continuously monitors specified repositories for new pull requests, analyzes code changes for quality, security vulnerabilities, and typos, and then posts detailed comments or approvals directly on the pull request.

### Key Features
*   **Automated PR Monitoring:** Automatically detects and reviews new pull requests in configured GitHub repositories.
*   **Comprehensive Code Review:** Performs AI-powered analysis for:
    *   **Code Quality:** Identifies best practice violations, potential bugs, and readability issues.
    *   **Security:** Detects common vulnerabilities like hardcoded secrets, SQL injection risks, and weak cryptography.
    *   **Typo & Grammar:** Checks for spelling and grammatical errors in code and comments.
*   **Intelligent Commenting:** Posts inline comments on specific lines for issues found and provides a summary comment for the entire PR.
*   **Configurable Review Scope:** Allows setting limits on the number of files and lines reviewed per pull request.
*   **AI Provider Flexibility:** Supports both OpenAI and Anthropic models for AI-driven reviews.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests where no issues are detected.
*   **Dry Run Mode:** Supports a dry run mode to simulate reviews without posting actual comments.

### Inputs
*   **Environment Variables:**
    *   `GITHUB_TOKEN`: Personal Access Token for GitHub API authentication.
    *   `AI_PROVIDER`: Choice of AI service ("openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor (e.g., `owner/repo,owner/repo2`).
    *   `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`: Boolean flags to enable/disable specific review types.
    *   `AUTO_APPROVE_MINOR`: Boolean flag to enable/disable automatic approval of clean PRs.
    *   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum lines per file to review.
    *   `AGENT_NAME`: The name used by the agent in PR comments.
    *   `POLLING_INTERVAL`: Frequency (in seconds) for checking new PRs.
*   **Command-line Arguments:**
    *   `start`: Initiates continuous monitoring.
        *   `--config-file`: Path to the configuration file (default: `.env`).
        *   `--dry-run`: Runs without posting comments.
        *   `--verbose`: Enables detailed logging.
    *   `review`: Reviews a specific pull request.
        *   `repo_url`: The URL of the repository (e.g., `https://github.com/owner/repo`).
        *   `pr_number`: The pull request number.
        *   `--config-file`: Path to the configuration file.
        *   `--dry-run`: Runs without posting comments.
    *   `setup`: Interactive wizard to generate a basic `.env` configuration file.

### Outputs
*   **GitHub Pull Request Comments:**
    *   **Inline Comments:** Detailed findings on specific lines of code with suggested improvements for typos, code quality, and security issues.
    *   **Summary Comments:** A comprehensive overview of all issues found in the pull request, posted as a general comment.
    *   **Approval Comments:** A message indicating no issues were found, potentially leading to automatic approval if configured.