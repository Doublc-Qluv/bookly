from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.schemas import Book, BookUpdateModel
from src.books.book_data import books

book_router = APIRouter()

@book_router.get('/', response_model=List[Book])
async def get_books():
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get('/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        detail="Book not found", 
        status_code=status.HTTP_404_NOT_FOUND
    )

@book_router.patch('/{book_id}')
async def update_book(book_id: int, book_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book.update(book_data.model_dump())
            return {"message": "Book updated"}
    raise HTTPException(
        detail="Book not found", 
        status_code=status.HTTP_404_NOT_FOUND
    )

@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(
        detail="Book not found", 
        status_code=status.HTTP_404_NOT_FOUND
    )
