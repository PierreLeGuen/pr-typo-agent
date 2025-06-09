FROM python:3.12-slim-bookworm

WORKDIR /app

# Install uv, a fast Python package installer and resolver
RUN pip install --no-cache-dir uv

# Copy pyproject.toml to define project dependencies
COPY pyproject.toml ./

# Install project dependencies. This will also make the 'pr-review-agent' script available.
RUN uv sync

# Copy the application source code
# The pr_review_agent directory contains the core logic and the __init__.py with the main entry point.
COPY pr_review_agent/ ./pr_review_agent/

# The application is a Typer CLI app.
# The `pr-review-agent` script is installed by `uv sync` based on pyproject.toml.
ENTRYPOINT ["pr-review-agent"]

# Default command if no arguments are provided to the entrypoint
# This will start the agent in polling mode by default
CMD ["start"]