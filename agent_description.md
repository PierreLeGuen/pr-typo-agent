## PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process for GitHub Pull Requests. It monitors specified repositories for new or updated PRs and provides comprehensive feedback on code quality, security, and potential typos.

### Main Functions

*   **Automated PR Review**: Continuously monitors designated GitHub repositories for open pull requests, initiating reviews automatically based on configured settings.
*   **On-Demand PR Review**: Allows users to trigger a review for a specific pull request by providing its repository URL and PR number.
*   **Comprehensive Code Analysis**:
    *   **Typo and Grammar Detection**: Identifies spelling and grammatical errors in new or modified code lines and comments, suggesting corrections.
    *   **Code Quality Review**: Utilizes advanced AI models (OpenAI or Anthropic) to assess code for best practices, readability, performance, and potential bugs.
    *   **Security Vulnerability Scanning**: Scans for common security issues such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic practices.
*   **GitHub Integration**: Posts detailed inline comments directly on the relevant lines of code and provides a comprehensive summary comment on the pull request.
*   **Configurable Review Behavior**: Offers extensive customization options for review types, AI provider selection, review scope (max files/lines), and auto-approval for clean PRs.
*   **Interactive Setup**: Includes a command-line utility to guide users through the initial configuration process.

### Inputs

*   **GitHub Pull Requests**: The agent consumes pull request data, including file changes (diffs), from GitHub via its API.
*   **Configuration**: Operational parameters, API keys, and review preferences are loaded from environment variables, typically from a `.env` file.

### Outputs

*   **GitHub Pull Request Comments**: The primary output consists of comments posted directly on GitHub pull requests, including:
    *   Inline comments for specific findings (e.g., typos, code quality suggestions, security alerts).
    *   A summary comment providing an overview of the review and detected issues.
*   **Console Output**: Provides logs and status updates during the agent's operation.

### Key Details

*   Requires a GitHub Personal Access Token with repository permissions.
*   Integrates with either OpenAI or Anthropic API for AI-powered reviews, requiring a corresponding API key.
*   Supports a "dry-run" mode for testing reviews without posting comments to GitHub.
*   Can be configured to automatically approve pull requests if no issues are found.
*   Allows setting limits on the number of files and lines reviewed per pull request to manage processing scope.