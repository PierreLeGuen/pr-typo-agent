FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy pyproject.toml and install dependencies
# This allows Docker to cache the dependency layer
COPY pyproject.toml ./
COPY pr_review_agent/ ./pr_review_agent/

# Install the project and its dependencies
RUN pip install --no-cache-dir .

# Command to run the application
# The `start` command is the default for continuous monitoring
CMD ["pr-review-agent", "start"]