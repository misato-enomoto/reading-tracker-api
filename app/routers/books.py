from fastapi import APIRouter
from app.schemas.book import Book, BookCreate

router = APIRouter()

books = []

@router.post("/books", response_model=Book)
def create_book(book: BookCreate):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    }
    books.append(new_book)
    return new_book


@router.get("/books", response_model=list[Book])
def get_books():
    return books
