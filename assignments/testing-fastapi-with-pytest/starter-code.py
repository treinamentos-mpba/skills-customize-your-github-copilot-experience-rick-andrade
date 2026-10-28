from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str


app = FastAPI(title="Book API")
books: list[Book] = []


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return books


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book) -> Book:
    books.append(book)
    return book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
