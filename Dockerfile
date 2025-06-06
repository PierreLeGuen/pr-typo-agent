FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy all project files into the Docker image.
# This ensures that `pip install .` can find the `pyproject.toml`
# and the `pr_review_agent` package source code.
COPY . .

# Install the project and its dependencies.
# The `.` refers to the current working directory (/app),
# where `pyproject.toml` and the `pr_review_agent` package are located.
RUN pip install . --no-cache-dir

# The application is run via the 'pr-review-agent' script,
# which is defined in pyproject.toml and installed by 'pip install .'.
# The 'start' command activates the agent's monitoring loop.
CMD ["pr-review-agent", "start"]