import secrets

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status

from app import settings

auth_header_scheme = APIKeyHeader(name="x-api-key")


class NotAuthenticatedException(HTTPException):
    def __init__(self):
        message = "Not authenticated"
        super().__init__(status.HTTP_403_FORBIDDEN, detail=message)


def require_admin(api_key: str = Depends(auth_header_scheme)) -> None:
    if not secrets.compare_digest(
        api_key.encode("utf-8"),
        settings.API_KEY.get_secret_value().encode("utf-8"),
    ):
        raise NotAuthenticatedException
