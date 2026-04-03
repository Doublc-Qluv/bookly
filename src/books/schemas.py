from pydantic import BaseModel, Field

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