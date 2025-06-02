"""Configuration management for PR Review Agent"""

import os
from typing import Any, Dict

from dotenv import load_dotenv


def load_config(config_file: str = ".env") -> Dict[str, Any]:
    """Load configuration from environment file"""
    if os.path.exists(config_file):
        load_dotenv(config_file)

    config = {
        # GitHub settings
        "github_token": os.getenv("GITHUB_TOKEN", ""),
        "github_webhook_secret": os.getenv("GITHUB_WEBHOOK_SECRET"),
        # AI provider settings
        "ai_provider": os.getenv("AI_PROVIDER", "openai"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
        # Review settings
        "review_typos": os.getenv("REVIEW_TYPOS", "true").lower() == "true",
        "review_code_quality": os.getenv("REVIEW_CODE_QUALITY", "true").lower()
        == "true",
        "review_security": os.getenv("REVIEW_SECURITY", "true").lower() == "true",
        # Behavior settings
        "auto_approve_minor": os.getenv("AUTO_APPROVE_MINOR", "false").lower()
        == "true",
        "max_files_per_review": int(os.getenv("MAX_FILES_PER_REVIEW", "50")),
        "max_lines_per_file": int(os.getenv("MAX_LINES_PER_FILE", "1000")),
        # Repository settings
        "watched_repositories": [
            repo.strip()
            for repo in os.getenv("WATCHED_REPOSITORIES", "").split(",")
            if repo.strip()
        ],
        # Agent settings
        "agent_name": os.getenv("AGENT_NAME", "PR Review Bot"),
        "polling_interval": int(os.getenv("POLLING_INTERVAL", "300")),
        "max_retries": int(os.getenv("MAX_RETRIES", "3")),
    }

    # Validate required settings
    if not config["github_token"]:
        raise ValueError(
            "GitHub token is required. Set GITHUB_TOKEN environment variable."
        )

    if config["ai_provider"] == "openai" and not config["openai_api_key"]:
        raise ValueError("OpenAI API key is required when using OpenAI provider.")

    if config["ai_provider"] == "anthropic" and not config["anthropic_api_key"]:
        raise ValueError("Anthropic API key is required when using Anthropic provider.")

    return config
