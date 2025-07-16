### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors designated GitHub repositories for new or updated pull requests and performs comprehensive reviews based on configurable criteria.

**Main Functions:**

*   **Automated Pull Request Monitoring**: Continuously checks specified GitHub repositories for open pull requests that require review.
*   **Intelligent Code Review**:
    *   **Typo and Grammar Correction**: Identifies and suggests corrections for spelling and grammatical errors within code and documentation.
    *   **AI-Powered Code Quality Analysis**: Leverages advanced AI models (OpenAI or Anthropic) to assess code quality, adherence to best practices, and potential performance issues.
    *   **Security Vulnerability Detection**: Scans for common security risks such as hardcoded secrets, potential SQL injection, and command injection vulnerabilities.
*   **Detailed Feedback**: Posts specific, actionable comments directly on the relevant lines of code within the pull request, including suggested improvements.
*   **Review Summaries**: Provides a concise summary of all findings in a main comment on the pull request.
*   **Optional Auto-Approval**: Can be configured to automatically approve pull requests that pass all review checks without any detected issues.
*   **On-Demand Review**: Allows users to trigger a review for a specific pull request by providing its repository URL and pull request number.

**Inputs:**

*   **GitHub API**: Receives pull request information, including changed files and diffs.
*   **Environment Variables**: Configures GitHub authentication, AI provider API keys, a list of repositories to monitor, review preferences (e.g., enable/disable typo, code quality, or security reviews), and operational parameters like polling intervals and review limits.
*   **Command Line**: Accepts repository URL and pull request number for single PR reviews, and flags for dry-run or verbose logging.

**Outputs:**

*   **GitHub Pull Request Comments**: Posts inline comments on specific code lines, a general summary comment, or an approval message.
*   **Console/Logs**: Displays agent status, progress, and error messages.