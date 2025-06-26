### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new or updated pull requests and performs comprehensive reviews, identifying potential issues related to typos, code quality, and security vulnerabilities. Based on its findings, the agent posts detailed comments directly on the pull request or approves it if no issues are detected.

#### Key Features

*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review**: Utilizes large language models (LLMs) from OpenAI or Anthropic to assess code quality and identify potential issues.
*   **Comprehensive Review Types**:
    *   **Typo and Grammar Check**: Reviews new code for spelling and grammatical errors.
    *   **Code Quality Analysis**: Identifies best practice violations, performance issues, and potential bugs.
    *   **Security Vulnerability Detection**: Scans for common security risks like hardcoded secrets, SQL injection, and command injection.
*   **Intelligent Commenting**: Posts detailed inline comments for specific findings and a summary comment on the pull request.
*   **Conditional Approval**: Can be configured to automatically approve pull requests if no issues are detected.
*   **Configurable Scope**: Allows setting limits on the number of files and lines reviewed per pull request.
*   **On-Demand Review**: Supports reviewing a specific pull request by providing its repository URL and PR number.

#### Inputs

*   **GitHub API**: Fetches pull request details, files, and existing comments.
*   **Environment Variables**: Configuration parameters such as GitHub token, AI provider API keys, watched repositories, review preferences (e.g., `REVIEW_TYPOS`, `REVIEW_CODE_QUALITY`, `REVIEW_SECURITY`), and agent behavior (e.g., `AUTO_APPROVE_MINOR`, `POLLING_INTERVAL`).
*   **Command Line (for on-demand review)**: Repository URL and PR number for specific pull request reviews.

#### Outputs

*   **GitHub Pull Request Comments**: Posts detailed feedback as inline comments on specific lines of code and a summary comment on the pull request. The agent's comments will appear under the configured `AGENT_NAME` (default: "PR Review Bot").
*   **GitHub Pull Request Approvals**: Submits an approval if configured and no issues are found.
*   **Console/Log Output**: Provides operational logs and status updates during its execution.