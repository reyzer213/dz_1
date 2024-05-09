# db/models.py

from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    pages: int

class BookCreate(BookBase):
    author_id: int

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
