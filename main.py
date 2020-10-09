import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import  Session
from app.db.events import  get_db

from app.api import routers


app = FastAPI()
app.include_router(routers.router,prefix="/apiv1")


@app.get("/")
async def hello():
    return "hello,world"



if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, debug=True)