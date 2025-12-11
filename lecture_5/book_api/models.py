from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# base class for all ORM models
Base = declarative_base()


class Book(Base):
    """
    SQLAlchemy ORM model representing a book record.

    table
        books

    fields
        id      primary key
        title   book title (required)
        author  book author (required)
        year    publication year (optional)
    """

    __tablename__ = "books"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, nullable=False)
    author: str = Column(String, nullable=False)
    year: int | None = Column(Integer, nullable=True)
