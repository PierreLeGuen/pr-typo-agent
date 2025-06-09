FROM python:3.12-slim-bookworm

WORKDIR /app

COPY pyproject.toml ./
COPY . .

RUN pip install .

CMD ["pr-review-agent", "start"]