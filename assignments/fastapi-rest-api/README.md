# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a production-ready REST API using the FastAPI framework. You'll create an API for managing a simple book library, implementing core RESTful operations, data validation, and error handling. This assignment will teach you the fundamentals of modern API development with automatic documentation and type safety.

## 📝 Tasks

### 🛠️ Task 1: Create a Basic FastAPI Application with Endpoints

#### Description

Set up a FastAPI application with a simple in-memory data structure to store books. Create GET and POST endpoints to retrieve and add books to the library. Start with basic functionality and hardcoded data.

#### Requirements

Completed program should:

- Create a FastAPI application instance
- Define a list to store book data in memory (dictionaries with id, title, author, year fields)
- Implement a GET `/books` endpoint that returns all books
- Implement a POST `/books` endpoint that accepts a new book and adds it to the list
- Include at least 2 sample books in the initial data
- Run the server on `localhost:8000` and test all endpoints

### 🛠️ Task 2: Add Data Validation with Pydantic Models

#### Description

Replace the dictionary-based approach with Pydantic models to ensure data validation and type safety. Create request and response models that enforce the book structure and automatically validate input data.

#### Requirements

Completed program should:

- Create a `Book` Pydantic model with fields: id (int), title (str), author (str), year (int)
- Create a `BookCreate` model without the id field for POST requests
- Update GET `/books` to return a list of `Book` objects
- Update POST `/books` to accept a `BookCreate` object
- FastAPI automatically returns validation errors when invalid data is sent
- View the auto-generated API documentation at `/docs`

### 🛠️ Task 3: Implement Full CRUD Operations

#### Description

Extend the API with complete CRUD (Create, Read, Update, Delete) operations. Add endpoints to retrieve a specific book by ID, update an existing book, and delete a book from the library.

#### Requirements

Completed program should:

- Implement GET `/books/{book_id}` to retrieve a single book by ID
- Implement PUT `/books/{book_id}` to update an existing book
- Implement DELETE `/books/{book_id}` to delete a book
- Each endpoint should work correctly with the in-memory data structure
- The DELETE endpoint should return a success message after removal
- Test all CRUD operations using FastAPI's interactive documentation

### 🛠️ Task 4: Add Error Handling and HTTP Status Codes (Stretch Goal)

#### Description

Improve the API's robustness by adding proper error handling and HTTP status codes. Ensure that appropriate status codes are returned for different scenarios (success, not found, validation errors, etc.).

#### Requirements

Completed program should:

- Return 404 status code when a book is not found in GET, PUT, or DELETE operations
- Return 201 status code for successful POST requests (creation)
- Return 200 status code for successful GET and PUT requests
- Return 204 status code for successful DELETE requests
- Raise `HTTPException` with appropriate status codes when operations fail
- Include meaningful error messages in responses
- All endpoints should handle edge cases gracefully
