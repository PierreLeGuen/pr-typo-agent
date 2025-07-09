### PR Review Agent

**Description:**
An AI-powered agent for automated code review and typo detection on GitHub pull requests. It monitors specified repositories for new pull requests, reviews code quality, security, and typos, and posts comments or approvals based on its findings.

**Features:**
*   **Automated PR Monitoring:** Continuously checks configured GitHub repositories for new or updated pull requests.
*   **Comprehensive Code Review:**
    *   **Typo and Grammar Review:** Identifies and suggests corrections for spelling and grammar errors in new code and comments.
    *   **AI-Powered Code Quality Review:** Leverages AI models (OpenAI or Anthropic) to analyze code for quality, best practices, performance, and potential bugs.
    *   **Security Vulnerability Detection:** Scans for common security risks like hardcoded secrets, SQL injection, command injection, and weak cryptographic algorithms.
*   **Intelligent Feedback:** Posts detailed inline comments on specific lines with issues and provides a summary comment for the entire pull request.
*   **Automated Approval:** Can be configured to automatically approve pull requests where no issues are detected.
*   **Configurable Review Scope:** Allows setting limits on the maximum number of files and lines reviewed per pull request.
*   **Flexible AI Integration:** Supports both OpenAI and Anthropic as AI service providers.
*   **Dry-Run Mode:** Enables testing the agent's review capabilities without posting actual comments to GitHub.
*   **On-Demand Review:** Can be triggered to review a specific pull request by its URL and number.

**Inputs:**
*   **GitHub Pull Requests:** Monitored from specified repositories.
*   **Configuration:** Provided via environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`, etc.).

**Outputs:**
*   **GitHub Comments:** Posts inline comments on specific lines of code and summary comments on pull requests.
*   **GitHub Approvals:** Submits approval status for pull requests if configured and no issues are found.
*   **Console Logs:** Provides operational status and error messages.