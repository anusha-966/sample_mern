from fastapi import FastAPI
app=FastAPI()

@app.get("/getStudents")
def getStudents():
    return "get student method called"

@app.post("/addStudent")
def addStudent():
    return "add student method called"
#localhost:8000/updateStudent
@app.put("/upadateStudent")
def updateStudent():
    return "update student method called"
#localhost:8000/deleteStudent

@app.delete("/deleteStudent")
def deleteStudent():
    return "delete student method called"
#localhost:8000/getparticularStudent/5
@app.get("/getparticularStudent/{userid}")
def getparticularStudent(user:int):
    return{"userid":userid}

@app.get("/getdeptdetails")
def getdeptdetails(dept:str,mark:int):
    return {"dept":dept,"mark":mark}
    

