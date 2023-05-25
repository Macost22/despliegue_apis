from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_api3():
    return {"message": "API 3"}

