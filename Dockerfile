FROM python:3.12-slim-bookworm

WORKDIR /app

# Install system dependencies required for some Python packages (e.g., pyspellchecker's editdistance)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and the source code directory
# pyproject.toml defines the project and its dependencies
# pr_review_agent/ is the actual Python package
COPY pyproject.toml ./
COPY pr_review_agent pr_review_agent/

# Install the project and its dependencies
RUN pip install .

# Command to run the application
# The `pr-review-agent` script is installed by `pip install .`
# The default command for the agent is `start` to monitor repositories.
CMD ["pr-review-agent", "start"]