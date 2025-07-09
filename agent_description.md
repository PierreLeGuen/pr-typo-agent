### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It actively monitors specified repositories for new pull requests, performing comprehensive reviews for code quality, security vulnerabilities, and potential typos. Based on its findings, the agent posts detailed comments directly on the pull request, providing actionable feedback to developers.

**Key Features:**
*   **Automated PR Monitoring:** Continuously checks designated GitHub repositories for new pull requests.
*   **AI-Powered Code Review:** Utilizes AI models (OpenAI or Anthropic) to analyze code for quality, best practices, and potential bugs.
*   **Security Vulnerability Detection:** Identifies common security risks such as hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
*   **Typo and Grammar Correction:** Scans new code and comments for spelling and grammar errors, suggesting corrections.
*   **Configurable Review Types:** Allows users to enable or disable specific review categories (typos, code quality, security).
*   **Automated Approvals:** Can be configured to automatically approve pull requests where no issues are detected.
*   **Detailed Feedback:** Posts inline comments on specific lines of code and provides a comprehensive summary comment on the pull request.
*   **Scalable Review Scope:** Configurable limits on the maximum number of files and lines reviewed per pull request.
*   **Flexible Operation:** Can run continuously to monitor repositories or review a specific pull request on demand.

**Inputs:**
*   **Environment Variables:** Configured via environment variables (often loaded from a `.env` file) for GitHub authentication (`GITHUB_TOKEN`), AI provider selection (`AI_PROVIDER`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`), watched repositories (`WATCHED_REPOSITORIES`), and various review and behavior settings (e.g., `REVIEW_TYPOS`, `AUTO_APPROVE_MINOR`, `MAX_FILES_PER_REVIEW`, `POLLING_INTERVAL`, `AGENT_NAME`).
*   **Command Line Arguments (for on-demand review):**
    *   Repository URL (e.g., `https://github.com/owner/repo`)
    *   Pull Request Number

**Outputs:**
*   **GitHub Pull Request Comments:** Posts detailed review comments, including inline suggestions on specific lines and a summary of findings, directly to the GitHub pull request.
*   **GitHub Pull Request Approvals:** Submits an approval status to the pull request if configured to auto-approve and no issues are found.
*   **Console/Log Output:** Provides operational status, debug information, and error messages to the standard output.