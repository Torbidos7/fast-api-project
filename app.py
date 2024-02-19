from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Alice",
        "age": 16,
        "class": "year 11"
    }
}

@app.get("/")
def index():
    return {"name":"First data"}

@app.get("/get-student/{student_id}")
# Path parameters are required by default, but you can make them optional by providing a default value. gt=0 means greater than 0.
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    return students[student_id]

#Optional query, the * will make the order of the parameters not matter 
@app.get("/get-by-name_optional/")
def get_student_optional(*, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]
    return {"Data": "Not found"}

