FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy pyproject.toml and the application source directory
# This allows pip install . to find the local package 'pr_review_agent'
COPY pyproject.toml ./
COPY pr_review_agent/ pr_review_agent/

# Install Python dependencies including the local package
RUN pip install --no-cache-dir .

# The application uses environment variables for configuration,
# which are expected to be provided at runtime.
# No ENV instructions are needed in the Dockerfile.

# Command to run the application
# The pyproject.toml defines a script 'pr-review-agent'
# The default command is 'start' as per pr_review_agent/__init__.py
CMD ["pr-review-agent", "start"]