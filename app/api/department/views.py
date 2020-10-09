from app.api.routers import router
from sqlalchemy.orm import Session
from app.models.models import Department
from app.api.department.schema import DepartmentCreate
from app.db.events import connection_db

import traceback
import time

db = connection_db()
@router.get("/department/hello")
async def hello():
    return "hello, department"


@router.get("/department/{department_id}")
async def department(department_id:int):
    try:
        dep_obj = db.query(Department).filter_by(id = department_id).first()
        return  dep_obj
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.get("/departments")
async def get_departments():
    try:
        dep_objs = db.query(Department).all()
        return {"code":200, "data":dep_objs}
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.post("/department")
async  def create_department(item:DepartmentCreate):
    try:
        db_department = db.query(Department).filter_by(name=item.name).first()
        if db_department:
            return {"code":200, "msg": "department已存在"}
        db_dep = Department(name=item.name)
        db.add(db_dep)
        db.commit()
        db.refresh(db_dep)
        return db_dep
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.delete("/department/{department_id}")
async def delete_department(department_id: int):
    try:
        pass
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}

