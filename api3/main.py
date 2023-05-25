from fastapi import FastAPI

app = FastAPI()

@app.get("/api3")
def read_api3():
    return {"message": "API 3"}

