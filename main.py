from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

@app.get("/")
def default_response():
    return {"message":"Server is running"}

@app.post("/register")
def create_user():
    return 

@app.get("/birthdays")
def get_all_birthdays():
    return 


@app.post("/create_birthday")
def create_birthday():
    return

@app.post("/edit_birthday")
def update_birthday():
    return
