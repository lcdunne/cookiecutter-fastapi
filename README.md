# Cookiecutter FastAPI

Scaffolds a FastAPI server with configurable size, database support, and test setup.

This is how I have grown used to organising FastAPI projects - it might not be for everyone. It serves mainly for me to avoid having to do all the same stuff repetitively. Hopefully it is useful.

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
sudo chmod +x setup.sh start.sh
./setup.sh
```

The `setup.sh` script will install all dependencies according to the dependency manager chosen during the cookiecutter generation.

You will be prompted for the following when generating a project:

- **dependency_manager**: `poetry` or `pip`
- **project_size**: `small` (flat structure) or `large` (layered structure)
- **database**: `sqlite`, `postgresql`, or `none`
- **include_tests**: `yes` or `no`

Note that if PostgreSQL is chosen, and tests are included, a separate database will be created for the tests. If your project is called `myproj`, then there will be a `myproj` and a `myproj_test` database. An in-memory database is used for SQLite tests.

## Directory structure

### Small project

```
.
├── app
│   ├── config.py
│   ├── database.py       # only if a database was selected
│   ├── dependencies.py
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── docker
│   ├── entrypoint.sh
│   └── init.sql          # only if postgresql
├── tests                 # only if include_tests == yes
│   ├── conftest.py
│   └── test_index.py
├── docker-compose.yaml
├── Dockerfile
├── logging_config.yaml
├── pytest.ini            # only if include_tests == yes
├── setup.sh
└── start.sh
```

### Large project

```
.
├── app
│   ├── api
│   │   ├── dependencies
│   │   │   ├── auth.py
│   │   │   └── db.py     # only if a database was selected
│   │   └── routes
│   │       └── index.py
│   ├── client
│   ├── database          # only if a database was selected
│   │   ├── lifecycle.py
│   │   ├── models.py
│   │   └── session.py
│   ├── exceptions
│   │   ├── domain.py
│   │   ├── handlers.py
│   │   └── http.py
│   ├── middleware
│   ├── repository
│   │   └── index.py
│   ├── schemas
│   │   ├── queries.py
│   │   └── response.py
│   ├── services
│   │   └── index.py
│   ├── utils
│   ├── config.py
│   ├── __init__.py
│   └── main.py
├── docker
│   ├── entrypoint.sh
│   └── init.sql          # only if postgresql
├── tests                 # only if include_tests == yes
│   ├── conftest.py
│   └── test_index.py
├── docker-compose.yaml
├── Dockerfile
├── logging_config.yaml
├── pytest.ini            # only if include_tests == yes
├── setup.sh
└── start.sh
```

## Running

To run with Docker:

```sh
docker compose up --build
```

To run locally (assuming the db is accessible):

```sh
./start.sh
```

When running locally, if using PostgreSQL, you will need to make sure the database is accessible. For example, by running `docker compose up db` you will just run the database service.

Navigate to `http://localhost:8000/docs` to explore the API docs.

## Running the tests

Just call `pytest` with the virtual environment active.
