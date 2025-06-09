FROM python:3.12-slim-bookworm

WORKDIR /app

# Install uv, a fast Python package installer and resolver
RUN pip install uv

# Copy the project's dependency definition file and source code
COPY pyproject.toml ./
COPY pr_review_agent/ ./pr_review_agent/

# Install Python dependencies defined in pyproject.toml, including the project itself
# The '--system' flag installs into the base Python environment provided by the image.
RUN uv pip install --system .

# Define the entry point for the application.
# The pyproject.toml defines 'pr-review-agent' as the script entry point.
ENTRYPOINT ["pr-review-agent"]