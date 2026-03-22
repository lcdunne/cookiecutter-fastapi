ARG PYTHON_VERSION=3.12
ARG POETRY_VERSION=2.2.1

FROM lcdunne/python-poetry:${PYTHON_VERSION}-poetry${POETRY_VERSION} AS builder

COPY poetry.lock pyproject.toml ./

RUN $POETRY_HOME/bin/poetry install --no-root --without dev && \
    rm -rf $POETRY_CACHE_DIR

FROM python:${PYTHON_VERSION}-slim

ENV VIRTUAL_ENV=/opt/virtualenvs/venv

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

COPY app app

COPY ./docker/entrypoint.sh logging_config.yaml pyproject.toml ./

RUN chmod +x ./entrypoint.sh
RUN chown -R appuser:appuser /app

USER appuser

ENV PATH="$VIRTUAL_ENV/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]
