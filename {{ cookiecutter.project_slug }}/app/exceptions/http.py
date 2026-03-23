from fastapi import HTTPException
from starlette import status


class UnauthorizedBasicException(HTTPException):
    def __init__(self):
        detail = "Incorrect username or password"
        headers = {"WWW-Authenticate": "Basic"}
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)


class UnauthorizedBearerException(HTTPException):
    def __init__(self):
        detail = "Invalid credentials"
        headers = {"WWW-Authenticate": "Bearer"}
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)


class NotAuthenticatedException(HTTPException):
    def __init__(self):
        message = "Not authenticated"
        super().__init__(status.HTTP_403_FORBIDDEN, detail=message)
