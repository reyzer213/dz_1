from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates
from db import database, models, crud

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/{author_id}/")
def get_books_by_author(author_id: int, db: Session = Depends(get_db)):
    books = crud.get_books_by_author(db, author_id)
    if not books:
        raise HTTPException(status_code=404, detail="No books found for this author")
    return books

@app.put("/books/{book_id}/")
def update_book_pages(book_id: int, new_pages: int, db: Session = Depends(get_db)):
    return crud.update_book_pages(db, book_id, new_pages)

@app.delete("/books/{book_id}/")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
