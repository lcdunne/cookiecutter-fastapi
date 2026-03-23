from typing import Literal

from pydantic import BaseModel, Field


class PaginationParameters(BaseModel):
    limit: int = Field(25, gt=0, le=25)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    order: Literal["asc", "desc"] = "desc"
