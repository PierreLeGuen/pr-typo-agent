FROM python:3.12-slim-bookworm

WORKDIR /app

# Install uv, the dependency manager specified in pyproject.toml
RUN pip install uv

# Copy pyproject.toml first to leverage Docker cache
COPY pyproject.toml ./

# Copy the application source code
# This makes the 'pr_review_agent' package available for installation by uv
COPY pr_review_agent/ ./pr_review_agent/
COPY hello.py ./hello.py

# Install project dependencies using uv, which reads pyproject.toml
# The '.' refers to the current directory, which contains pyproject.toml and the pr_review_agent package
# --system installs into the system Python environment, not a virtual environment
# --no-cache-dir reduces image size by not storing build artifacts
RUN uv pip install --system --no-cache-dir .

# Command to run the application
# The pyproject.toml defines 'pr-review-agent' as a script pointing to 'pr_review_agent:main'
# The `start` command is defined in pr_review_agent/__init__.py
CMD ["pr-review-agent", "start"]