FROM python:3.11-slim

RUN pip install poetry==1.6.1

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY ./pyproject.toml ./README.md ./poetry.lock .

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./src .

EXPOSE 8080

ENTRYPOINT uvicorn ragtalk.app.server:app --host 0.0.0.0 --port 8080
