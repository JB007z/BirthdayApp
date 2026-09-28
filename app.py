from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default_response():
    return {"message":"Server running"}


@app.get("/birthdays")
def get_birthdays():
    return {"Birthdays":["01/03/2000","20/3/2002"]}