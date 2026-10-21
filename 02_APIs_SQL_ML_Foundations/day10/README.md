# Day 10 — API Fundamentals and FastAPI

## Overview

This project introduces HTTP APIs, JSON data, HTTP status codes, Python HTTP requests, and building REST API endpoints using FastAPI.

## Learning Objectives

- Understand APIs and common HTTP methods.
- Convert Python dictionaries to JSON and JSON to Python objects.
- Make GET requests using the `requests` library.
- Handle request timeouts, connection errors, and HTTP errors.
- Build API endpoints using FastAPI.
- Use path parameters and Pydantic models.
- Validate incoming JSON request bodies.
- Handle HTTP 404 and 409 errors.
- Store and retrieve student records using temporary in-memory storage.

## Project Structure

```text
day10/
├── api_basics.py
├── README.md
└── FAST_API/
    └── main.py
```

## Technologies

- Python
- Requests
- FastAPI
- Uvicorn
- Pydantic
- JSON
- HTTP

## Run the API

From the `FAST_API` directory, run:

```powershell
python -m uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve one student |
| POST | `/students` | Validate and create a student |

## Example POST Request

```json
{
  "id": 5,
  "name": "Neha",
  "score": 88
}
```

## Validation and Error Handling

- `200 OK`: Request succeeded.
- `404 Not Found`: Student ID does not exist.
- `409 Conflict`: Student ID already exists.
- `422 Unprocessable Content`: Input validation failed.

## Storage Limitation

Student records are stored in a Python list in memory. Newly created records are temporary and reset when the server process restarts. Persistent database storage will be introduced in a later phase.

## What I Practiced

- Making HTTP requests and reading JSON responses.
- Handling HTTP errors.
- Creating GET and POST endpoints.
- Validating data with Pydantic.
- Testing endpoints with Swagger UI.
- Preventing duplicate student IDs.
