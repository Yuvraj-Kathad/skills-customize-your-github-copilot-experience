from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI application
app = FastAPI(title="Book Library API", description="A simple API for managing books")

# Sample data - initially populated with two books
books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
]

# Counter for generating new book IDs
next_book_id = 3


# Define Pydantic models for data validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


# TODO: Implement Task 1 - Basic endpoints
# GET /books - return all books
# POST /books - add a new book


# TODO: Implement Task 3 - CRUD operations
# GET /books/{book_id} - get a specific book
# PUT /books/{book_id} - update a book
# DELETE /books/{book_id} - delete a book


# TODO: Add error handling and appropriate status codes (Task 4)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
