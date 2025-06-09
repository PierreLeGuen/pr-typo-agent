FROM python:3.12-slim-bookworm

WORKDIR /app

COPY pyproject.toml ./
COPY pr_review_agent/ ./pr_review_agent/

RUN pip install .

CMD ["pr-review-agent", "start"]