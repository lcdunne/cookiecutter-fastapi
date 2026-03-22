import secrets
{% if cookiecutter.database != "none" %}
from collections.abc import Generator

{% endif %}
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
{% if cookiecutter.database != "none" %}
from sqlalchemy.orm import Session
{% endif %}
from starlette import status

from app import settings
{% if cookiecutter.database != "none" %}
from app.database import SessionLocal
{% endif %}


auth_header_scheme = APIKeyHeader(name="x-api-key")


class NotAuthenticatedException(HTTPException):
    def __init__(self):
        message = "Not authenticated"
        super().__init__(status.HTTP_403_FORBIDDEN, detail=message)


{% if cookiecutter.database != "none" %}
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


{% endif %}
def require_admin(api_key: str = Depends(auth_header_scheme)) -> None:
    """Validate the super-admin (developer) API key."""
    if not secrets.compare_digest(
        api_key.encode("utf-8"),
        settings.API_KEY.get_secret_value().encode("utf-8"),
    ):
        raise NotAuthenticatedException
