{% if cookiecutter.project_size == "small" %}
from fastapi import Depends, FastAPI, HTTPException
{% if cookiecutter.database != "none" %}
from sqlalchemy import text
from sqlalchemy.orm import Session
{% endif %}
from app import settings
from app.dependencies import require_admin{% if cookiecutter.database != "none" %}, get_db{% endif %}
from app.schemas import ServerStatus

app = FastAPI(title=settings.APPLICATION_NAME)


@app.get("/_health")
async def health() -> ServerStatus:
    return ServerStatus(status=1)


{% if cookiecutter.database != "none" %}
@app.get("/_db_health")
def db_health(db: Session = Depends(get_db)) -> ServerStatus:
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return ServerStatus(status=1)


{% endif %}
@app.get("/protected", dependencies=[Depends(require_admin)])
async def protected() -> ServerStatus:
    return ServerStatus(status=1)
{% else %}
from fastapi import FastAPI

from app import settings
from app.api import router
from app.exceptions.handlers import register_exception_handlers


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APPLICATION_NAME)
    app.include_router(router)
    register_exception_handlers(app)
    return app
{% endif %}
