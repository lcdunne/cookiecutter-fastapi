{% if cookiecutter.database != "none" %}
from sqlalchemy.orm import Session

from app.repository import index as index_repo
{% endif %}
from app.schemas import ServerStatus


def health() -> ServerStatus:
    return ServerStatus(status="ok")

{% if cookiecutter.database != "none" %}

def db_health(db: Session) -> ServerStatus:
    index_repo.ping(db)
    return ServerStatus(status="ok")
{% endif %}
