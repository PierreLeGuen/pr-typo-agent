# PR Review Agent

The PR Review Agent is an AI-powered tool designed to automate and enhance the code review process on GitHub. It monitors specified repositories for new pull requests and provides comprehensive feedback on code quality, potential security vulnerabilities, and grammatical/spelling errors.

## Summary
This agent automates pull request reviews by leveraging AI models and pattern-based checks. It identifies issues such as typos, code quality concerns, and security flaws, then posts detailed comments directly on GitHub pull requests. It can be configured to monitor multiple repositories and customize the types of reviews performed.

## Key Features
*   **Automated PR Monitoring**: Continuously checks configured GitHub repositories for new or updated pull requests.
*   **AI-Powered Code Review**: Utilizes OpenAI or Anthropic models to assess code quality and suggest improvements.
*   **Typo and Grammar Detection**: Identifies and suggests corrections for spelling and grammar errors in code and documentation.
*   **Security Vulnerability Scanning**: Detects common security patterns and potential vulnerabilities like hardcoded secrets, SQL injection risks, and weak cryptography.
*   **Detailed Feedback**: Posts inline comments for specific issues and a summary comment for the entire pull request.
*   **Configurable Review Types**: Allows enabling or disabling typo, code quality, and security reviews independently.
*   **Specific PR Review**: Can be triggered to review a single pull request on demand.
*   **Dry Run Mode**: Supports running reviews without posting actual comments to GitHub.
*   **Auto-Approval (Optional)**: Can be configured to automatically approve pull requests if no issues are found.

## How it Works
The agent operates by periodically polling the configured GitHub repositories for open pull requests. For each new or unreviewed PR, it fetches the changed files and their content (diffs). It then passes these changes through its configured reviewers:
1.  **Typo Reviewer**: Checks newly added lines for spelling and grammar mistakes, optionally using an LLM for more accurate suggestions.
2.  **Security Reviewer**: Scans new code for predefined security patterns and flags potential vulnerabilities.
3.  **AI Code Quality Reviewer**: If enabled, sends relevant code snippets to the chosen AI provider (OpenAI or Anthropic) for a comprehensive code quality assessment.

After all reviews are complete, the agent compiles the findings and posts them as comments on the GitHub pull request. If no issues are found and auto-approval is enabled, it posts an approval comment.

## Inputs
*   **Environment Variables**: Configuration is primarily done via environment variables (e.g., `GITHUB_TOKEN`, `AI_PROVIDER`, `WATCHED_REPOSITORIES`, `REVIEW_TYPOS`, `MAX_FILES_PER_REVIEW`, etc.). These can be loaded from a `.env` file.
*   **Command Line Arguments (for specific PR review)**:
    *   `repo_url`: The URL of the GitHub repository (e.g., `https://github.com/owner/repo`).
    *   `pr_number`: The number of the pull request to review.

## Outputs
*   **GitHub Pull Request Comments**:
    *   Inline comments on specific lines of code where issues are detected (e.g., typos, security flaws, code quality suggestions).
    *   A summary comment on the pull request detailing the types and counts of issues found, or an approval message if no issues are present.
*   **Console/Log Output**: Provides real-time status updates, debug information, and error messages during operation.