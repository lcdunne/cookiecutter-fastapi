from app.core.logging import get_logger
from app.database import engine, models

logger = get_logger(__name__)


def init_db() -> None:
    models.Base.metadata.create_all(bind=engine)


def teardown_db() -> None:
    models.Base.metadata.drop_all(bind=engine)


def shutdown_db() -> None:
    engine.dispose()
