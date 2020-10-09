from pydantic import BaseModel

class TroubleCreate(BaseModel):
    title: str
    department_id: int
    troubletype_id: int
