from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app import settings


def get_engine() -> Engine:
    """Create and return a new SQLAlchemy engine instance."""
    connect_args = {}
    db_url = settings.DATABASE_URL.get_secret_value()
    is_sqlite = db_url.startswith("sqlite")

    if is_sqlite:
        connect_args["check_same_thread"] = False

    return create_engine(
        db_url,
        connect_args=connect_args,
        echo=settings.DATABASE_ECHO,
        pool_pre_ping=not is_sqlite,
    )


def get_session_factory(engine: Engine) -> sessionmaker[Session]:
    """Create and return a new sessionmaker factory bound to the given engine."""
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)
