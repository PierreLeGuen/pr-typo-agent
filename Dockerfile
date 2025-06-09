FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

# Copy pyproject.toml first to leverage Docker cache for dependency installation
COPY pyproject.toml ./

# Copy the entire application source code into the working directory.
# This is crucial for `pip install .` to find the package source (e.g., pr_review_agent directory).
COPY . .

# Install the project and its dependencies.
# The '--no-cache-dir' flag reduces image size by not storing pip's cache.
# The '--upgrade pip' ensures pip is up-to-date.
# `pip install .` will install the 'pr-typo-agent' package and make the 'pr-review-agent' script available.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

# Define the default command to run the application.
# Based on `pyproject.toml` and `pr_review_agent/__init__.py`, the main entry point is `pr-review-agent start`.
CMD ["pr-review-agent", "start"]