from typing import Callable

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from starlette import status

from app.exceptions.domain import (
    CoreException,
    InputException,
    ResourceConflictException,
    ResourceNotFoundException,
)
from app.schemas.response import ApiErrorResponse


async def request_validation_exception_handler(
    _: Request, exc: RequestValidationError
) -> Response:
    # NOTE: the auto-generated OpenAPI docs do not respect exception handlers...
    #   see here: https://github.com/fastapi/fastapi/discussions/9061
    error_response = ApiErrorResponse(
        detail=jsonable_encoder(exc.errors(), exclude={"input"})
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=error_response.model_dump(),
    )


def _handle(status_code: int, *messages: str) -> Response:
    response = ApiErrorResponse(detail=list(messages))
    return JSONResponse(response.model_dump(), status_code)


async def _handler_400(_: Request, exc: CoreException) -> Response:
    return _handle(status.HTTP_400_BAD_REQUEST, exc.message)


async def _handler_404(_: Request, exc: ResourceNotFoundException) -> Response:
    return _handle(status.HTTP_404_NOT_FOUND, exc.message)


async def _handler_409(_: Request, exc: ResourceNotFoundException) -> Response:
    return _handle(status.HTTP_409_CONFLICT, exc.message)


async def _handler_500(_: Request, exc: Exception) -> Response:
    return _handle(
        status.HTTP_500_INTERNAL_SERVER_ERROR, "Something went wrong on our side."
    )


def register_exception_handlers(app: FastAPI) -> None:
    register_handler(app, RequestValidationError, request_validation_exception_handler)
    register_handler(app, InputException, _handler_400)
    register_handler(app, ResourceNotFoundException, _handler_404)
    register_handler(app, ResourceConflictException, _handler_409)
    register_handler(app, CoreException, _handler_500)


def register_handler(app: FastAPI, exc: type[Exception], handler: Callable) -> None:
    app.add_exception_handler(exc, handler)
