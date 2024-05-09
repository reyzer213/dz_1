from sqlalchemy.orm import Session
from . import models

def get_author(db_session: Session, author_id: int):
    return db_session.query(models.Author).filter(models.Author.id == author_id).first()

def get_authors(db_session: Session, skip: int = 0, limit: int = 10):
    return db_session.query(models.Author).offset(skip).limit(limit).all()

def create_author(db_session: Session, author: models.AuthorCreate):
    db_author = models.Author(name=author.name)
    db_session.add(db_author)
    db_session.commit()
    db_session.refresh(db_author)
    return db_author

def get_books_by_author(db_session: Session, author_id: int):
    return db_session.query(models.Book).filter(models.Book.author_id == author_id).all()

def create_book(db_session: Session, book: models.BookCreate):
    db_book = models.Book(**book.dict())
    db_session.add(db_book)
    db_session.commit()
    db_session.refresh(db_book)
    return db_book

def update_book_pages(db_session: Session, book_id: int, new_pages: int):
    db_book = db_session.query(models.Book).filter(models.Book.id == book_id).first()
    db_book.pages = new_pages
    db_session.commit()
    return db_book

def delete_book(db_session: Session, book_id: int):
    db_book = db_session.query(models.Book).filter(models.Book.id == book_id).first()
    db_session.delete(db_book)
    db_session.commit()
