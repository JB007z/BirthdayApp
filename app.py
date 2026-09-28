from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default_response():
    return {"message":"Server running"}


@app.get("/birthdays")
def get_birthdays():
    return {"Birthdays":["01/03/2000","20/3/2002"]}

@app.post("/create_birthday")
def create_birthday():
    return {"birthday":"test123"}

@app.patch("/update_birthday")
def update_birthday():
    return {"birthday_updated":"test123"}

@app.delete("/delete_birthday")
def delete_birthday():
    return {"birthday_deleted":"test123"}
