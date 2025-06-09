# PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests and performs comprehensive automated reviews, providing feedback directly on GitHub.

## Main Functions

*   **Automated PR Monitoring**: Watches configured GitHub repositories for new or updated pull requests.
*   **Multi-faceted Code Review**: Conducts various types of reviews:
    *   **Typo and Grammar Check**: Identifies and suggests corrections for spelling and grammar errors in code comments, documentation, and string literals.
    *   **AI-powered Code Quality Review**: Utilizes large language models (LLMs) to analyze code for quality, best practices, performance issues, and potential bugs.
    *   **Security Vulnerability Detection**: Scans for common security risks such as hardcoded secrets, SQL injection patterns, command injection, and weak cryptographic algorithms.
*   **GitHub Integration**: Posts detailed inline comments on specific lines of code and provides a comprehensive summary comment on the pull request.
*   **On-Demand Review**: Allows users to trigger a review for a specific pull request manually via a command-line interface.
*   **Configurable Behavior**: Highly customizable through environment variables to enable/disable specific review types, set review limits, and define monitoring preferences.

## Key Features

*   **AI Integration**: Supports OpenAI and Anthropic LLMs for advanced code analysis and typo correction.
*   **Granular Control**: Users can enable or disable typo, code quality, and security reviews independently.
*   **Scalability**: Configurable limits for the number of files and lines reviewed per PR to manage API usage and review scope.
*   **Dry-Run Mode**: Allows testing the agent's review capabilities without posting actual comments to GitHub.
*   **Interactive Setup**: Provides a command-line utility to guide users through initial configuration.

## Inputs

*   **Configuration**: Environment variables loaded from a `.env` file (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `REVIEW_TYPOS`, `WATCHED_REPOSITORIES`, etc.).
*   **GitHub Pull Requests**: The agent processes pull request data (code changes, files, comments) fetched from the GitHub API.
*   **Command Line Arguments (stdin)**: Used for starting the agent (`start`), reviewing a specific PR (`review`), or setting up the configuration (`setup`).

## Outputs

*   **GitHub Comments (HTTP)**:
    *   **Inline Review Comments**: Detailed feedback posted directly on specific lines within changed files.
    *   **Summary Comments**: A consolidated review summary posted as a general comment on the pull request.
*   **Console Logs (stdout)**: Provides real-time status updates, warnings, and error messages about the agent's operations.