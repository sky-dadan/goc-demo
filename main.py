import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import routers


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routers.router,prefix="/apiv1")


@app.get("/")
async def hello():
    return "hello,world"



if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, debug=True)