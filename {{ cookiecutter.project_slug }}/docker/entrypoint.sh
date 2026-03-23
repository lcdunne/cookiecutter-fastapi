#!/bin/sh

set -e

exec uvicorn {% if cookiecutter.project_size == "large" %}app.main:create_app --factory{% else %}app.main:app{% endif %} \
    --host 0.0.0.0 \
    --port 8000 \
    --log-config=logging_config.yaml
