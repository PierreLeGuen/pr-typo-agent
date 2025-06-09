### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new or updated Pull Requests and provides comprehensive feedback on code quality, security, and typos.

**Main Functions:**

*   **Automated PR Monitoring:** Automatically detects and reviews new Pull Requests in configured GitHub repositories.
*   **Intelligent Code Review:** Utilizes advanced AI models (OpenAI or Anthropic) to analyze code for:
    *   **Code Quality:** Identifies best practice violations, potential bugs, and areas for improvement.
    *   **Security Vulnerabilities:** Detects common security risks such as hardcoded secrets, SQL injection, command injection, and weak cryptography.
    *   **Typo and Grammar Checks:** Scans new code for spelling and grammatical errors, providing suggestions for correction.
*   **Detailed Feedback:** Posts inline comments directly on GitHub Pull Requests for specific issues and provides a summarized review comment for the entire PR.
*   **Configurable Review Scope:** Allows setting limits on the number of files and lines reviewed per PR to manage review load.
*   **Optional Auto-Approval:** Can be configured to automatically approve Pull Requests if no issues are found.
*   **On-Demand Review:** Supports reviewing a specific Pull Request manually via a command-line interface.
*   **Interactive Setup:** Provides a guided setup process to configure essential settings.

**Inputs:**

*   **Configuration:** Environment variables (loaded from a `.env` file) specifying GitHub token, AI API keys, AI provider choice, watched repositories, review preferences (e.g., enable/disable typo, code quality, security reviews), maximum file/line limits, polling interval, and agent name.
*   **GitHub Data (via API polling):** Pull Request details, including changed files and their content (patches).
*   **Command Line Arguments (stdin):** Repository URL and Pull Request number for manual review commands.

**Outputs:**

*   **GitHub Comments (HTTP):** Detailed inline comments on specific lines of code within a Pull Request, and a summary comment posted on the Pull Request discussion thread.
*   **Console Output (stdout):** Status updates, logs, and error messages during agent operation.