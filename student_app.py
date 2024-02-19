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

# Pydantic model , it will validate the data
class Student(BaseModel):
    name: str 
    age: int
    class_: str

# Pydantic model for updating data, 
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    class_: Optional[str] = None


    
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

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.class_ != None:
        students[student_id].class_ = student.class_
    return students[student_id]