from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel, Field
from uuid import UUID
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        


class Book(BaseModel):
    # id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


BOOKS = []


@app.get("/")
def read_api(db:Session=Depends(get_db)):
    return db.query(models.Books).all()


@app.post("/")
def create_book(book: Book,db:Session=Depends(get_db)):
    
    book_models=models.Books() #(title=book.title,author=book.author,description=book.description,rating=book.rating)
    book_models.title=book.title
    book_models.author=book.author
    book_models.description=book.description
    book_models.rating=book.rating
    db.add(book_models)
    
    db.commit()
    
    # BOOKS.append(book)
    return book


@app.put("/{book_id}")
def update_book(book_id: int, book: Book,db:Session=Depends(get_db)):
    counter = 0
    book_models=db.query(models.Books).filter(models.Books.id==book_id).first()
    
    
    
    
    
    # for x in BOOKS:
    #     counter += 1
    #     if x.id == book_id:
    #         BOOKS[counter - 1] = book
    #         return BOOKS[counter - 1]
    if book_models is None:    
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )
        
    book_models.title=book.title
    book_models.author=book.author
    book_models.description=book.description
    book_models.rating=book.rating
    db.add(book_models)
    db.commit()
    
    return book


@app.delete("/{book_id}")
def delete_book(book_id: int,db:Session=Depends(get_db)):
    
    book_models=db.query(models.Books).filter(models.Books.id==book_id).first()
    #check if key exist or not exist
    
    if book_models is None:    
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )
    db.query(models.Books).filter(models.Books.id==book_id).delete()
    db.commit()
    
    
    
    
    
    # counter = 0

    # for x in BOOKS:
    #     counter += 1
    #     if x.id == book_id:
    #         del BOOKS[counter - 1]
    #         return f"ID: {book_id} deleted"
    