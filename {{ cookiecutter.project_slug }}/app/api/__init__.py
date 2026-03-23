from fastapi.routing import APIRouter

from app.api.routes import index

router = APIRouter()
router.include_router(index.router)
