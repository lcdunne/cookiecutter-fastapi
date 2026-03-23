from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
{% if cookiecutter.database != "none" %}
from sqlalchemy.orm import Session
{% endif %}
from app.api.dependencies import require_admin{% if cookiecutter.database != "none" %}, get_db{% endif %}
from app.schemas import ServerStatus
from app.schemas.response import ApiResponse
from app.services import index as index_svc

router = APIRouter(tags=["Index"])


@router.get("/_health")
async def health() -> ApiResponse[ServerStatus]:
    return ApiResponse(data=index_svc.health())


{% if cookiecutter.database != "none" %}
@router.get("/_db_health")
def db_health(db: Session = Depends(get_db)) -> ApiResponse[ServerStatus]:
    try:
        return ApiResponse(data=index_svc.db_health(db))
    except Exception:
        raise HTTPException(status_code=503, detail="Database unavailable")


{% endif %}
@router.get("/protected", dependencies=[Depends(require_admin)])
async def protected() -> ApiResponse[ServerStatus]:
    return ApiResponse(data=index_svc.health())
