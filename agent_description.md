### PR Review Agent

The PR Review Agent is an AI-powered automation tool designed for comprehensive code review on GitHub pull requests. It continuously monitors specified repositories for new pull requests, automatically analyzing code for quality, potential security vulnerabilities, and grammatical/spelling errors. Based on its findings, the agent posts detailed comments directly on the pull request or approves it if no issues are detected.

#### Key Features

*   **Automated PR Monitoring**: Watches configured GitHub repositories for new and updated pull requests.
*   **Multi-faceted Code Review**:
    *   **AI-Powered Code Quality**: Leverages OpenAI or Anthropic models to assess code quality, adherence to best practices, and potential bugs.
    *   **Security Analysis**: Identifies common security vulnerabilities such as hardcoded secrets, SQL injection risks, and weak cryptographic algorithms.
    *   **Typo and Grammar Check**: Reviews new or changed lines for spelling and grammatical errors, offering suggestions.
*   **Intelligent Commenting**: Posts inline comments for specific code issues and provides a summarized review comment on the pull request.
*   **Conditional Approval**: Can be configured to automatically approve pull requests that pass all checks without issues.
*   **Configurable Review Scope**: Allows setting limits on the number of files and lines reviewed per pull request.
*   **Flexible AI Integration**: Supports both OpenAI and Anthropic as AI providers.
*   **Manual Review Capability**: Can be triggered to review a specific pull request on demand.

#### Inputs

*   **GitHub Pull Requests**: The agent processes new and open pull requests from configured repositories.
*   **Environment Variables**: Configuration is primarily managed through environment variables, which can be loaded from a `.env` file. These include GitHub authentication tokens, AI API keys, repository lists, and various review settings.
*   **Command-Line Arguments**: For on-demand review of a specific PR (repository URL, PR number).

#### Outputs

*   **GitHub Pull Request Comments**:
    *   **Inline Comments**: Detailed feedback posted directly on specific lines of code within the pull request diff.
    *   **Summary Comments**: A comprehensive summary of findings posted as a general comment on the pull request.
    *   **Approval Comments**: Messages indicating successful review and approval when no issues are found.
*   **Console Logs**: Provides real-time status updates, warnings, and error messages during operation.