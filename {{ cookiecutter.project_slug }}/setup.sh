#!/bin/sh
set -e

DEPS="fastapi pydantic pydantic-settings python-dotenv uvicorn pyyaml{% if cookiecutter.database == 'sqlite' %} sqlalchemy{% elif cookiecutter.database == 'postgresql' %} sqlalchemy psycopg2-binary{% endif %}"
DEV_DEPS="black isort pytest pytest-random-order mkdocs"

{% if cookiecutter.dependency_manager == "poetry" %}
echo "Setting up with Poetry..."

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

echo "Formatting code..."
poetry run isort . --quiet
poetry run black . --quiet
{% else %}
echo "Setting up with pip..."

python -m venv .venv
. .venv/bin/activate
pip install $DEPS $DEV_DEPS
pip freeze > requirements.txt

echo "Formatting code..."
isort . --quiet
black . --quiet
{% endif %}

cp .env.example .env
