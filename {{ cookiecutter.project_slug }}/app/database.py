from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app import settings


class Base(DeclarativeBase):
    pass


def get_engine() -> Engine:
    """Create and return a new SQLAlchemy engine instance."""
    connect_args = {}
    db_url = settings.DATABASE_URL.get_secret_value()
    is_sqlite = db_url.startswith("sqlite")

    if is_sqlite:
        connect_args["check_same_thread"] = False

    if db_url == "sqlite:///:memory:":
        return create_engine(db_url, connect_args=connect_args, poolclass=StaticPool)

    return create_engine(
        db_url,
        connect_args=connect_args,
        echo=settings.DATABASE_ECHO,
        pool_pre_ping=not is_sqlite,
    )


def get_session_factory(engine: Engine) -> sessionmaker[Session]:
    """Create and return a new sessionmaker factory bound to the given engine."""
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)


engine = get_engine()
SessionLocal = get_session_factory(engine)
