from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from models import Book
from schemas import BookCreate, BookResponse

app = FastAPI(title="Book API")


@app.get("/books/", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)) -> List[BookResponse]:
    """
    return all books from the database.
    soft 404: empty list = ok.
    """
    return db.query(Book).all()


@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(data: BookCreate, db: Session = Depends(get_db)) -> BookResponse:
    """
    create a new book.
    no model_dump() — assigning manual fields is perfectly valid.
    """
    book = Book(
        title=data.title,
        author=data.author,
        year=data.year
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)) -> None:
    """
    delete by ID.
    hard 404 → book does not exist.
    """
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()


@app.put("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_book(book_id: int, data: BookCreate, db: Session = Depends(get_db)) -> BookResponse:
    """
    update an existing book.
    """
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = data.title
    book.author = data.author
    book.year = data.year

    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search", response_model=List[BookResponse])
def search_books(
    title: Optional[str] = Query(None, description="Filter by title"),
    author: Optional[str] = Query(None, description="Filter by author"),
    year: Optional[int] = Query(None, description="Filter by year"),
    db: Session = Depends(get_db)
) -> List[BookResponse]:
    """
    search books using AND logic.
    if no matches → empty list.
    """
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year is not None:
        query = query.filter(Book.year == year)

    return query.all()