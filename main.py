import uvicorn
from fastapi import FastAPI
from containers import Container
from upbits.interface.controllers.upbit_controllers import router as upbitprice_routers

app = FastAPI()
app.container = Container()
app.include_router(upbitprice_routers)

@app.get("/")
def hello():
    return {"hello": "FastAPI"}

if __name__ == "__name__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)