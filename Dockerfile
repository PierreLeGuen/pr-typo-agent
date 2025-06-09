FROM python:3.12-slim-bookworm

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY pyproject.toml ./
COPY pr_review_agent/ ./pr_review_agent/

RUN pip install --no-cache-dir .

ENTRYPOINT ["pr-review-agent"]
CMD ["start"]