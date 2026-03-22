#!/bin/sh
set -e

DEPS="fastapi pydantic pydantic-settings python-dotenv uvicorn pyyaml{% if cookiecutter.database == 'sqlite' %} sqlalchemy{% elif cookiecutter.database == 'postgresql' %} sqlalchemy psycopg2-binary{% endif %}"
DEV_DEPS="black isort pytest pytest-random-order mkdocs"

MANAGER="${1}"

setup_with_poetry() {
    poetry init --no-interaction \
        --name "{{ cookiecutter.project_slug }}" \
        --description "{{ cookiecutter.description }}" \
        --author "{{ cookiecutter.author }} <{{ cookiecutter.author_email }}>"

    cat >> pyproject.toml << 'EOF'

[tool.poetry]
package-mode = false

[tool.isort]
profile = "black"

[tool.pytest.ini_options]
addopts = "--random-order"
EOF

    poetry add $DEPS
    poetry add --group dev $DEV_DEPS
    poetry install
    poetry run black .
    poetry run isort .

}

setup_with_pip() {
    python -m venv .venv
    . .venv/bin/activate
    pip install $DEPS $DEV_DEPS
    pip freeze > requirements.txt
    black .
    isort .
}

case "$MANAGER" in
    poetry)
        echo "Setting up with Poetry..."
        setup_with_poetry
        ;;
    pip)
        echo "Setting up with pip..."
        setup_with_pip
        ;;
    *)
        echo "Usage: $0 [poetry|pip]"
        exit 1
        ;;
esac

cp .env.example .env
