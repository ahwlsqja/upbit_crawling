import uvicorn
from fastapi import FastAPI
# from middlewares import create_middlewares

app = FastAPI()


@app.get("/")
def hello():
    return {"hello": "FastAPI"}

if __name__ == "__name__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)