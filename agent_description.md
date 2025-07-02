### PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub pull requests. It continuously monitors specified repositories for new or updated pull requests, performing comprehensive reviews based on configurable criteria.

**Key Features:**

*   **Automated Code Review:** Automatically analyzes pull requests for various issues.
*   **Configurable Review Types:**
    *   **Typo and Grammar Review:** Identifies and suggests corrections for spelling and grammar errors in code and comments.
    *   **AI-Powered Code Quality Review:** Uses large language models (OpenAI or Anthropic) to assess code quality, readability, performance, and best practices.
    *   **Security Vulnerability Review:** Detects common security patterns like hardcoded secrets, potential SQL injection, and command injection risks.
*   **GitHub Integration:** Interacts directly with GitHub to fetch PR details, files, and post comments.
*   **Detailed Feedback:** Posts inline comments on specific lines of code where issues are found, along with a comprehensive summary comment on the pull request.
*   **Optional Auto-Approval:** Can be configured to automatically approve pull requests if no issues are detected.
*   **Flexible Operation:** Can operate in a continuous polling mode to monitor repositories or be triggered to review a specific pull request manually.
*   **Dry-Run Mode:** Allows testing the agent's review capabilities without posting actual comments to GitHub.

**Inputs:**

*   **Configuration:** Environment variables (e.g., GitHub token, AI API keys, watched repositories, review preferences) loaded from a `.env` file or system environment.
*   **GitHub Pull Requests:** Fetches PR data (files, diffs, comments) via the GitHub API (HTTP).
*   **Command Line Arguments:** Used to specify the mode of operation (start monitoring or review a single PR) and configuration file path.

**Outputs:**

*   **GitHub Comments:** Posts inline review comments and a summary comment on the pull request (HTTP).
*   **GitHub Approvals:** Can submit pull request approvals (HTTP).
*   **Console Output:** Provides real-time logs, status updates, and error messages (stdout).

**Configuration:**

The agent is highly configurable via environment variables, allowing users to:

*   Specify GitHub Personal Access Token (`GITHUB_TOKEN`).
*   Choose between OpenAI or Anthropic for AI services (`AI_PROVIDER`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).
*   Enable or disable specific review types (typos, code quality, security).
*   Define a list of repositories to monitor (`WATCHED_REPOSITORIES`).
*   Set limits on the number of files and lines reviewed per PR.
*   Configure polling intervals and the agent's display name (`AGENT_NAME`).