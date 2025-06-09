### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process for GitHub Pull Requests. It monitors specified repositories for new or updated PRs and provides automated feedback on various aspects of the code.

#### Main Functions

*   **Automated PR Review**: Continuously monitors designated GitHub repositories for open pull requests.
*   **Multi-faceted Code Analysis**: Performs comprehensive reviews including:
    *   **Typo and Grammar Checking**: Identifies spelling and grammatical errors in code comments, documentation, and string literals.
    *   **AI-powered Code Quality Review**: Utilizes large language models (LLMs) to assess code quality, readability, performance, and adherence to best practices.
    *   **Security Vulnerability Detection**: Scans for common security issues such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
*   **Intelligent Commenting**: Posts detailed inline comments on specific lines of code where issues are found, along with a summary comment on the overall pull request.
*   **Configurable Behavior**: Allows users to enable/disable specific review types, set limits on file and line review counts, and configure auto-approval for clean PRs.
*   **Flexible AI Integration**: Supports both OpenAI and Anthropic API providers for AI-driven reviews.
*   **On-demand Review**: Can be triggered to review a specific pull request manually.

#### Inputs

*   **Configuration**: Environment variables (loaded from a `.env` file or system environment) to set GitHub tokens, AI API keys, watched repositories, review preferences, and agent behavior.
*   **GitHub API (Polling)**: Fetches pull request data, including files and comments, from monitored repositories.
*   **Command Line Interface (CLI)**:
    *   `start`: Initiates continuous monitoring of configured repositories.
    *   `review <repo_url> <pr_number>`: Reviews a specific pull request by its repository URL and number.
    *   `setup`: Provides an interactive prompt (stdin) to generate a basic `.env` configuration file.

#### Outputs

*   **GitHub Comments**: Posts review comments directly on pull requests, including inline suggestions and a comprehensive summary of findings.
*   **Console Output (stdout)**: Provides logs and status updates on the agent's operations, including errors and review progress.