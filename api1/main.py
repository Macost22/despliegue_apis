from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_api1():
    return {"message": "API 1"}

