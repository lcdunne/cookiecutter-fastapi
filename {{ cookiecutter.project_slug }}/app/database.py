from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app import settings


def get_engine() -> Engine:
    """Create and return a new SQLAlchemy engine instance."""
    connect_args = {}
    is_sqlite = settings.DATABASE_URL.startswith("sqlite")

    if is_sqlite:
        connect_args["check_same_thread"] = False

    return create_engine(
        settings.DATABASE_URL,
        connect_args=connect_args,
        echo=settings.DATABASE_ECHO,
        pool_pre_ping=not is_sqlite,
    )


def get_session_factory(engine: Engine) -> sessionmaker[Session]:
    """Create and return a new sessionmaker factory bound to the given engine."""
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)


engine = get_engine()
SessionLocal = get_session_factory(engine)
