from fastapi import Depends, FastAPI
{% if cookiecutter.database != "none" %}
from sqlalchemy import text
from sqlalchemy.orm import Session
{% endif %}
from app import settings
from app.dependencies import require_admin{% if cookiecutter.database != "none" %}, get_db{% endif %}

app = FastAPI(title=settings.APPLICATION_NAME)


@app.get("/_health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

{% if cookiecutter.database != "none" %}
@app.get("/_db_health")
def db_health(db: Session = Depends(get_db)) -> dict[str, int]:
    result = db.execute(text("SELECT 1"))
    return {"status": result.scalar_one()}

{% endif %}
@app.get("/protected", dependencies=[Depends(require_admin)])
async def protected() -> dict[str, str]:
    return {"secret": "secret message"}