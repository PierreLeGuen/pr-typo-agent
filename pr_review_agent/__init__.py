#!/usr/bin/env python3
"""
PR Review Agent - AI-powered pull request review automation
"""

import asyncio
import os

import typer
from rich.console import Console
from rich.panel import Panel

from .agent import PRReviewAgent
from .config import load_config

console = Console()
app = typer.Typer(help="🤖 AI-powered PR Review Agent")


@app.command("start")
def start_agent(
    config_file: str = typer.Option(".env", help="Path to configuration file"),
    dry_run: bool = typer.Option(False, help="Run in dry-run mode"),
    verbose: bool = typer.Option(False, help="Enable verbose logging"),
):
    """Start monitoring repositories for new PRs"""
    console.print(
        Panel(
            "🤖 PR Review Agent Starting...", title="Agent Status", border_style="green"
        )
    )

    try:
        config = load_config(config_file)
        agent = PRReviewAgent(config, dry_run=dry_run, verbose=verbose)
        asyncio.run(agent.run())
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command("review")
def review_pr(
    repo_url: str = typer.Argument(..., help="Repository URL"),
    pr_number: int = typer.Argument(..., help="Pull request number"),
    config_file: str = typer.Option(".env", help="Path to configuration file"),
    dry_run: bool = typer.Option(False, help="Don't post actual comments"),
):
    """Review a specific pull request"""
    console.print(f"[blue]Reviewing PR #{pr_number} in {repo_url}[/blue]")

    try:
        config = load_config(config_file)
        agent = PRReviewAgent(config, dry_run=dry_run)
        asyncio.run(agent.review_single_pr(repo_url, pr_number))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command("setup")
def setup_config():
    """Interactive setup for agent configuration"""
    console.print(
        Panel("Setting up PR Review Agent...", title="Setup", border_style="blue")
    )

    github_token = typer.prompt("GitHub Personal Access Token", hide_input=True)
    ai_provider = typer.prompt(
        "AI Provider", default="openai", type=typer.Choice(["openai", "anthropic"])
    )

    if ai_provider == "openai":
        ai_token = typer.prompt("OpenAI API Key", hide_input=True)
    else:
        ai_token = typer.prompt("Anthropic API Key", hide_input=True)

    env_content = f"""# PR Review Agent Configuration
GITHUB_TOKEN={github_token}
AI_PROVIDER={ai_provider}
{"OPENAI_API_KEY" if ai_provider == "openai" else "ANTHROPIC_API_KEY"}={ai_token}
REVIEW_TYPOS=true
REVIEW_CODE_QUALITY=true
REVIEW_SECURITY=true
"""

    with open(".env", "w") as f:
        f.write(env_content)

    console.print("[green]✅ Configuration saved to .env[/green]")


def main():
    """Main entry point"""
    app()


if __name__ == "__main__":
    main()
