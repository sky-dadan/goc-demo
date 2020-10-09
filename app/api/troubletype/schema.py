from pydantic import  BaseModel

class TroubleTypeCreate(BaseModel):
    name: str
