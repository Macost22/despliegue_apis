from fastapi import FastAPI

app = FastAPI()

@app.get("/api1")
def read_api1():
    return {"message": "API 1"}

