# Cookiecutter FastAPI

Creates a small FastAPI server with optional database.

## Quickstart

Run the following, to create :

```sh
cookiecutter .
```

After following the prompts, `cd` into the new directory and run:

```sh
sudo chmod +x ./setup.sh ./start.sh
```

The `setup.sh` file will configure the project by installing the minimum dependencies needed for the FastAPI server. Currently only `pip` and `poetry` are supported.

The resulting directory structure will look like this:

```
.
├── app
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   ├── __init__.py
│   └── main.py
├── docker
│   └── entrypoint.sh
├── docker-compose.yaml
├── Dockerfile
├── logging_config.yaml
├── poetry.lock
├── pyproject.toml
├── README.md
├── setup.sh
└── start.sh
```

To run the app using docker, just call `docker compose up --build`. To test the application, navigate to `http://localhost:8000/docs` and hit the `_health` or `_db_health` endpoint.

## TODO

- Prompt for tests
- Prompt for "big or small" project
