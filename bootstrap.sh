#!/bin/sh
set -e

if ! command -v python3 > /dev/null 2>&1; then
    echo "python3 not found. Please install Python 3 and try again."
    exit 1
fi

VENV=$(mktemp -d)

echo "Creating virtual environment at $VENV..."
python3 -m venv "$VENV"

echo "Installing cookiecutter..."
"$VENV"/bin/pip install --quiet cookiecutter

"$VENV"/bin/cookiecutter gh:lcdunne/cookiecutter-fastapi < /dev/tty

echo "Removing virtual environment..."
rm -rf "$VENV"
echo "Done."
