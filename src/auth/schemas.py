from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from typing import List
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime


class UserBooksModel(UserModel):
    books: List[Book]
    reviews: List[ReviewModel]


class UserCreateModel(BaseModel):
    username: str = Field(max_length=16)
    email: str = Field(max_length=50)
    password: str = Field(min_length=6)
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)


class UserLoginModel(BaseModel):
    email: str = Field(max_length=50)
    password: str = Field(min_length=6)


class EmailModel(BaseModel):
    addresses: List[str]
