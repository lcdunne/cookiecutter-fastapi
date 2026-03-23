from typing import Generic, Self, TypeVar

from fastapi import Request
from pydantic import BaseModel, Field

from app.schemas.queries import PaginationParameters
from app.utils.time_util import get_now_formatted

T = TypeVar("T")


class PaginationMetadata(BaseModel):
    total: int
    next_page: str | None
    previous_page: str | None
    current_page: int
    page_size: int
    total_pages: int

    @classmethod
    def from_query(cls, q: PaginationParameters, total: int, request: Request) -> Self:
        current_page = (q.offset // q.limit) + 1
        total_pages = (total + q.limit - 1) // q.limit if q.limit > 0 else 0

        # Offset varies per request, wheras the other q params need to remain.
        base_url = request.url.remove_query_params("offset")
        next_page = None
        previous_page = None

        if q.offset + q.limit < total:
            next_offset = q.offset + q.limit
            next_page = str(base_url.include_query_params(offset=next_offset))

        if q.offset > 0:
            if q.offset >= total:
                # Calculates the maximum offset possible
                prev_offset = ((total - 1) // q.limit) * q.limit if total > 0 else 0
            else:
                prev_offset = max(0, q.offset - q.limit)
            previous_page = str(base_url.include_query_params(offset=prev_offset))

        return cls(
            total=total,
            current_page=current_page,
            page_size=q.limit,
            total_pages=total_pages,
            next_page=next_page,
            previous_page=previous_page,
        )


class ApiResponse(BaseModel, Generic[T]):
    data: T | None = None
    timestamp: str = Field(default_factory=get_now_formatted)


class ApiListResponse(ApiResponse[T]):
    pagination: PaginationMetadata | None = None

    def paginate(self, count: int, q: PaginationParameters, request: Request) -> Self:
        self.pagination = PaginationMetadata.from_query(q, count, request)
        return self


class ApiErrorResponse(BaseModel, Generic[T]):
    detail: T | None = None
    timestamp: str = Field(default_factory=get_now_formatted)

