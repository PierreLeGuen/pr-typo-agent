## PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new pull requests and performs comprehensive reviews, identifying potential issues related to code quality, security vulnerabilities, and typos. Based on its findings, the agent posts detailed comments or approvals directly on the pull request, streamlining development workflows.

### Key Features

*   **Automated PR Monitoring:** Continuously polls configured GitHub repositories for new pull requests awaiting review.
*   **Multi-faceted Code Review:**
    *   **AI-Powered Code Quality:** Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for best practices, readability, performance issues, and potential bugs.
    *   **Security Vulnerability Detection:** Scans code for common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
    *   **Typo and Grammar Correction:** Identifies and suggests corrections for spelling and grammar errors in new or changed code lines, optionally leveraging AI for more intelligent suggestions.
*   **Configurable Review Scope:** Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **Intelligent Filtering:** Automatically skips draft pull requests, excessively large pull requests, and non-code or ignored files to focus on relevant changes.
*   **Detailed Feedback:** Posts inline comments on specific lines of code where issues are found, including suggestions for improvement.
*   **Review Summaries:** Provides a consolidated summary of all findings directly on the pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests where no issues are detected.
*   **Customizable Agent Identity:** The name displayed in PR comments is configurable.

### Inputs

*   **Environment Variables:**
    *   `GITHUB_TOKEN`: Your GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: Specifies the AI service provider ("openai" or "anthropic").
    *   `OPENAI_API_KEY`: Your OpenAI API key (if `AI_PROVIDER` is "openai").
    *   `ANTHROPIC_API_KEY`: Your Anthropic API key (if `AI_PROVIDER` is "anthropic").
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
    *   `GITHUB_WEBHOOK_SECRET`: (Optional) Secret for validating GitHub webhook payloads.
    *   `REVIEW_TYPOS`: `true` or `false` to enable/disable typo review.
    *   `REVIEW_CODE_QUALITY`: `true` or `false` to enable/disable AI code quality review.
    *   `REVIEW_SECURITY`: `true` or `false` to enable/disable security review.
    *   `AUTO_APPROVE_MINOR`: `true` or `false` to automatically approve PRs with no issues.
    *   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
    *   `AGENT_NAME`: The name used by the agent in PR comments.
    *   `POLLING_INTERVAL`: How often (in seconds) to check for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
*   **CLI Arguments (via `pr-review-agent` command):**
    *   `start`: Initiates continuous monitoring.
    *   `review <repo_url> <pr_number>`: Reviews a specific pull request manually.
    *   `setup`: An interactive utility to help configure environment variables.

### Outputs

*   **GitHub API (Comments & Approvals):**
    *   Inline comments on pull request files, highlighting specific issues (typos, code quality, security) with messages and suggestions.
    *   Summary comments on the pull request, detailing overall findings.
    *   Approval comments on pull requests if configured for auto-approval and no issues are found.
*   **Console (stdout/stderr):**
    *   Logs of agent activity, review progress, and any encountered errors.