from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_api2():
    return {"message": "API 2"}

