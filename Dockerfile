FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy pyproject.toml and the application source
COPY pyproject.toml ./
COPY pr_review_agent/ pr_review_agent/

# Install application and its dependencies
RUN pip install .

# Set the default command to run the agent
CMD ["pr-review-agent", "start"]