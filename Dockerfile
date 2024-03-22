FROM python:3.11-slim

RUN pip install poetry==1.6.1

RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* ./README.md ./

RUN poetry install  --no-interaction --no-ansi --no-root

COPY ./src/ ./src

RUN poetry install --no-interaction --no-ansi

EXPOSE 8080

CMD exec uvicorn --app-dir=src/ragtalk app.server:app --host 0.0.0.0 --port 8080
