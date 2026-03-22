# Cookiecutter FastAPI

Creates a small FastAPI server with optional database support.

## Quickstart

The quickest way to use this is to run this script (feel free to check what it does first!):

```sh
curl -fsSL https://raw.githubusercontent.com/lcdunne/cookiecutter-fastapi/main/bootstrap.sh | sh
```

Alternatively, if you already have `cookiecutter` installed:

```sh
cookiecutter gh:lcdunne/cookiecutter-fastapi
```

After following the prompts, `cd` into the new directory and run:

```sh
chmod +x setup.sh start.sh
./setup.sh [poetry|pip]
```

## Directory structure

```
.
├── app
│   ├── config.py
│   ├── database.py       # only if a database was selected
│   ├── dependencies.py
│   ├── __init__.py
│   └── main.py
├── docker
│   └── entrypoint.sh
├── docker-compose.yaml
├── Dockerfile
├── logging_config.yaml
├── pyproject.toml        # only if using poetry
├── requirements.txt      # only if using pip
├── setup.sh
└── start.sh
```

## Running

To run with Docker:

```sh
docker compose up --build
```

To run locally:

```sh
./start.sh
```

Navigate to `http://localhost:8000/docs` to explore the API.

## TODO

- Prompt for tests
- Prompt for "big or small" project
