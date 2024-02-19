from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Giovanni",
        "age": 17,
        "class": "superiori"
    },
    2: {
        "name": "Alice",
        "age": 16,
        "class": "superiori"
    }
}

class Student(BaseModel):
    name: str
    age: int
    class_: str
    
@app.get("/")
def index():
    return {"name":"First data"}

@app.get("/get-student/{student_id}")
# Path parameters are required by default, but you can make them optional by providing a default value. gt=0 means greater than 0.
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    return students[student_id]

#Optional query, the * will make the order of the parameters not matter 
#Difference between query and path is that query is not in the endpoint
@app.get("/get-by-name_optional/{student_id}")
def get_student_optional(*, student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        # No duplicate students
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]