#!/usr/bin/sh

set -e

. ./.venv/bin/activate

if [ -f './.env' ]; then
  . ./.env
fi

uvicorn {% if cookiecutter.project_size == "large" %}app.main:create_app --factory{% else %}app.main:app{% endif %} --reload --log-config=logging_config.yaml