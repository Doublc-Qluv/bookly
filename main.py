from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2012-01-01",
        "page_count": 224,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django for Beginners",
        "author": "Markus K. Kuhnel",
        "publisher": "Packt Publishing",
        "published_date": "2012-01-01",
        "page_count": 320,
        "language": "English",
    },
    {
        "id": 3,
        "title": "FastAPI: Building Web APIs with FastAPI",
        "author": "Sebastián Ramírez",
        "publisher": "Packt Publishing",
        "published_date": "2022-01-01",
        "page_count": 320,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Python for Data Analysis",
        "author": "Wes McKinney",
        "publisher": "O'Reilly Media",
        "published_date": "2013-01-01",
        "page_count": 320,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Python for Data Science",
        "author": "Wes McKinney",
        "publisher": "O'Reilly Media",
        "published_date": "2014-01-01",
        "page_count": 320,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Python for Data Visualization",
        "author": "Wes McKinney",
        "publisher": "O'Reilly Media",
        "published_date": "2015-01-01",
        "page_count": 320,
        "language": "English",
    },
]

class Book(BaseModel):
    id: int = Field(description="The ID of the book")
    title: str = Field(description="The title of the book")
    author: str = Field(description="The author of the book")
    publisher: str = Field(description="The publisher of the book")
    published_date: str = Field(description="The published date of the book")
    page_count: int = Field(description="The page count of the book")
    language: str = Field(description="The language of the book")

class BookUpdateModel(BaseModel):
    title: str = Field(description="The title of the book")
    author: str = Field(description="The author of the book")
    publisher: str = Field(description="The publisher of the book")
    published_date: str = Field(description="The published date of the book")
    page_count: int = Field(description="The page count of the book")
    language: str = Field(description="The language of the book")


@app.get('/books', response_model=List[Book])
async def get_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/books/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        detail="Book not found", 
        status_code=status.HTTP_404_NOT_FOUND
    )

@app.patch('/books/{book_id}')
async def update_book(book_id: int, book_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book.update(book_data.model_dump())
            return {"message": "Book updated"}
    raise HTTPException(
        detail="Book not found", 
        status_code=status.HTTP_404_NOT_FOUND
    )

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(
        detail="Book not found", 
        status_code=status.HTTP_404_NOT_FOUND
    )
