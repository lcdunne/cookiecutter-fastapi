#!/usr/bin/sh

set -e

. ./.venv/bin/activate

if [ -f './.env' ]; then
  . ./.env
fi

uvicorn app.main:app --reload --log-config=logging_config.yaml