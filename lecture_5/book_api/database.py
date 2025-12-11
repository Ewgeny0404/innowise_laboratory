from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from models import Base

# connection string to the SQLite database (local file)
SQLALCHEMY_DATABASE_URL: str = "sqlite:///./books.db"

# echo=True for debugging: logs every SQL query. turn off in production.
engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    future=True,  # enables SQLAlchemy 2.0-style behavior
)

# session factory used to create database session objects
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# create all tables if they do not exist yet
Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a database session.

    usage
        db: Session = Depends(get_db)

    yields
        a single session per request, and ensures it is closed afterwards.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
