from pydantic import BaseModel


class ServerStatus(BaseModel):
    status: int
