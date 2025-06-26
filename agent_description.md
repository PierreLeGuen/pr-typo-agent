**Agent Name:** PR Review Agent

**Summary:**
The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It continuously monitors specified repositories for new pull requests, automatically reviewing them for code quality, potential security vulnerabilities, and typos. Based on its findings, the agent posts detailed comments on the pull request, providing actionable feedback, or approves the pull request if no issues are detected.

**Key Features:**
*   **Automated Pull Request Reviews:** Monitors configured GitHub repositories and automatically initiates reviews for new pull requests.
*   **Comprehensive Code Analysis:**
    *   **AI-Powered Code Quality Review:** Utilizes large language models (LLMs) to analyze code for adherence to best practices, potential bugs, and performance inefficiencies.
    *   **Security Vulnerability Detection:** Identifies common security risks such as hardcoded secrets, SQL injection patterns, and command injection vulnerabilities.
    *   **Typo and Grammar Checking:** Reviews code comments, documentation, and string literals for spelling and grammatical errors, offering corrections.
*   **Configurable Review Scope:** Allows users to enable or disable specific review types (typos, code quality, security) and set limits on the number of files and lines reviewed per pull request.
*   **Automated Approvals:** Can be configured to automatically approve pull requests that pass all enabled checks without any detected issues.
*   **Detailed Feedback:** Posts inline comments on specific lines of code where issues are found, along with a comprehensive summary comment on the pull request.
*   **Flexible AI Integration:** Supports integration with various AI providers (e.g., OpenAI, Anthropic) for intelligent analysis.
*   **Dry Run Mode:** Provides an option to simulate reviews without posting actual comments to GitHub, useful for testing configurations.

**Inputs:**
*   **Environment Variables:** The agent is configured primarily through environment variables, typically loaded from a `.env` file. These variables control GitHub authentication, AI service selection, monitored repositories, review preferences, and agent behavior.
    *   `GITHUB_TOKEN`: A GitHub Personal Access Token with `repo` permissions.
    *   `AI_PROVIDER`: Specifies the AI service provider (e.g., `openai`, `anthropic`).
    *   `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`: API key for the chosen AI provider.
    *   `WATCHED_REPOSITORIES`: A comma-separated list of GitHub repositories (e.g., `owner/repo,owner/repo2`) to monitor.
    *   `REVIEW_TYPOS`: `true` or `false` to enable/disable typo review.
    *   `REVIEW_CODE_QUALITY`: `true` or `false` to enable/disable AI code quality review.
    *   `REVIEW_SECURITY`: `true` or `false` to enable/disable security review.
    *   `AUTO_APPROVE_MINOR`: `true` or `false` to enable/disable automatic approvals.
    *   `MAX_FILES_PER_REVIEW`: Maximum number of files to review per PR.
    *   `MAX_LINES_PER_FILE`: Maximum lines to review per file.
    *   `AGENT_NAME`: The name the agent uses in PR comments.
    *   `POLLING_INTERVAL`: How often (in seconds) the agent checks for new PRs.
    *   `MAX_RETRIES`: Maximum retries for API calls.
    *   `GITHUB_WEBHOOK_SECRET`: (Optional) Secret for GitHub webhook validation.
*   **Command-line Arguments (stdin):**
    *   `pr-review-agent start`: Initiates the agent to continuously monitor repositories.
    *   `pr-review-agent review <repo_url> <pr_number>`: Triggers a review for a specific pull request on demand.
    *   `pr-review-agent setup`: Provides an interactive guide to generate a basic `.env` configuration file.

**Outputs:**
*   **GitHub Pull Request Comments (HTTP):** Posts inline comments on specific lines of code with detailed findings and suggested improvements.
*   **GitHub Pull Request Summary (HTTP):** Posts a general comment summarizing the overall review results for the pull request.
*   **GitHub Pull Request Approval (HTTP):** If configured, posts an approval comment on the pull request when no issues are found.
*   **Console Output (stdout):** Provides real-time logging information about the agent's operations, status, and any errors encountered.