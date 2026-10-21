from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    score: int


# Shared student data
students = [
    {"id": 1, "name": "Abhilash", "score": 95},
    {"id": 2, "name": "Priya", "score": 85},
    {"id": 3, "name": "Amit", "score": 92},
    {"id": 4, "name": "Rahul", "score": 72},
]

@app.get('/')
def home():
    return {"message" : "Welcome to my first API"}

@app.get('/students')
def get_students():
    return {"students": students}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student['id'] == student_id:
            return {"student": student}

    raise HTTPException(
        status_code=404,
        detail="Student not found."
    )

@app.post("/students")
def create_student(student: Student):
    new_student = student.model_dump()
    for existing_student in students:
        if existing_student["id"] == new_student["id"]:
            raise HTTPException(
                status_code=409,
                detail="Student ID already exists."
            )

    students.append(new_student)
    return {
        "message" :  "Student received successfully",
        "student" : new_student
    }