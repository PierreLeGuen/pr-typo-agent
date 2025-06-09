FROM python:3.12-slim-bookworm

WORKDIR /app

# Install build dependencies for Python packages with C extensions
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and the application source code
COPY pyproject.toml ./
COPY pr_review_agent/ ./pr_review_agent/

# Install the project and its dependencies as defined in pyproject.toml
RUN pip install --no-cache-dir .

# Command to run the application
CMD ["pr-review-agent", "start"]