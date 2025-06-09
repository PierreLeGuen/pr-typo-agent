FROM python:3.12-slim-bookworm

WORKDIR /app

# Install uv, a fast Python package installer and resolver
RUN pip install uv

# Copy pyproject.toml and the application source code
# This allows uv to find the project dependencies defined in pyproject.toml
COPY pyproject.toml ./
COPY pr_review_agent/ ./pr_review_agent/

# Install project dependencies using uv
# The '.' indicates to install the package in the current directory (which contains pyproject.toml)
# --system flag installs into the system Python environment, suitable for Docker
RUN uv pip install --system .

# Command to run the application
# The pyproject.toml defines a script `pr-review-agent = "pr_review_agent:main"`
# So, `pr-review-agent` should be available as a command after installation.
CMD ["pr-review-agent", "start"]