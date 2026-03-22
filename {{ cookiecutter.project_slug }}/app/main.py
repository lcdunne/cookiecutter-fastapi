from fastapi import FastAPI

from app import Settings


app = FastAPI(title=settings.APPLICATION_NAME)

@app.get("/_health")
async def health() -> dict[str, str]:
    return {"status": "ok"}