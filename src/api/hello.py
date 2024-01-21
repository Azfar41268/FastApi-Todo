from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello():
    return "Hello Wrold"
