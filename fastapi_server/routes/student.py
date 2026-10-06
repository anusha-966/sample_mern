
from fastapi import APIRouter

from database import student_collection

from models import Student_model


student_router = APIRouter(
    prefix="/student",
    tags=["student"]
)


# localhost:8000/student/addstudent

@student_router.post("/addstudent")
def addstudent(stu: Student_model):

    result = student_collection.insert_one(stu.model_dump())

    return "student inserted success"


# localhost:8000/student/getstudent

@student_router.get("/getstudent")
def getstudent():

    return "get student method called"

@student_router.put("/updatestudent")
def updatestudent():
    return "update student method called"


# localhost:8000/student/deletestudent

@student_router.delete("/deletestudent")
def deletestudent():

    return "delete student method called"

