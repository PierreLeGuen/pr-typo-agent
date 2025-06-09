### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the pull request review process on GitHub. It monitors specified repositories for new or updated pull requests and provides automated feedback on various aspects of the code.

#### Main Functions

*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for open pull requests.
*   **Comprehensive Code Review**: Performs automated analysis of pull request changes, identifying potential issues.
*   **AI-Powered Feedback**: Leverages large language models (LLMs) for advanced code quality assessment and intelligent typo/grammar corrections.
*   **Direct GitHub Integration**: Posts review comments and summaries directly to the pull request on GitHub.

#### Features

*   **Typo and Grammar Detection**: Identifies spelling and grammatical errors in new code or documentation lines.
*   **Code Quality Analysis**: Reviews code for best practices, readability, performance issues, and potential bugs using an AI provider (OpenAI or Anthropic).
*   **Security Vulnerability Scanning**: Detects common security concerns such as hardcoded secrets, SQL injection risks, command injection, and weak cryptographic algorithms.
*   **Configurable Review Scope**: Allows users to set limits on the number of files and lines reviewed per PR and enable/disable specific review types (typos, code quality, security).
*   **Flexible Deployment**: Can run in a continuous monitoring mode or be triggered to review a single, specific pull request on demand.
*   **Dry-Run Mode**: Supports a dry-run option to preview review comments without posting them to GitHub.
*   **Customizable Agent Name**: The name displayed in PR comments can be configured.

#### Inputs

*   **Environment Variables**: (via `.env` file or system environment)
    *   `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication.
    *   `AI_PROVIDER`: Choice of AI service ("openai" or "anthropic").
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: Comma-separated list of GitHub repositories to monitor.
    *   Flags for enabling/disabling specific review types (`REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`).
    *   Configuration for review limits (`MAX_FILES_PER_REVIEW`, `MAX_LINES_PER_FILE`), polling interval (`POLLING_INTERVAL`), and agent name (`AGENT_NAME`).
*   **Command Line Arguments**:
    *   `repo_url`: (for single PR review) The URL of the GitHub repository.
    *   `pr_number`: (for single PR review) The pull request number.

#### Outputs

*   **GitHub Pull Request Comments**: (via HTTP to GitHub API)
    *   Inline comments on specific lines of code detailing typos, code quality issues, or security vulnerabilities, often with suggestions.
    *   A summary comment on the pull request providing an overview of findings or an approval message if no issues are detected.