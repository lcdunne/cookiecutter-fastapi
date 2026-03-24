from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
{% if cookiecutter.database != "none" %}
from sqlalchemy import text
{% endif %}
{% if cookiecutter.project_size == "small" %}
{% if cookiecutter.database != "none" %}
from app.database import Base, engine
{% endif %}
from app.main import app as _app
{% else %}
{% if cookiecutter.database != "none" %}
from app.database import engine
from app.database.models import Base
{% endif %}
from app.main import create_app
{% endif %}

{% if cookiecutter.database != "none" %}
@pytest.fixture(scope="session", autouse=True)
def setup_database() -> Generator[None, None, None]:
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(autouse=True)
def clean_tables() -> Generator[None, None, None]:
    yield
    with engine.connect() as conn:
        for table in Base.metadata.sorted_tables:
{% if cookiecutter.database == "postgresql" %}
            conn.execute(text(f"TRUNCATE TABLE {table.name} RESTART IDENTITY CASCADE"))
{% elif cookiecutter.database == "sqlite" %}
            conn.execute(table.delete())
{% endif %}
        conn.commit()


{% endif %}
@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    {% if cookiecutter.project_size == "small" %}
    with TestClient(_app) as c:
    {% else %}
    with TestClient(create_app()) as c:
    {% endif %}
        yield c
