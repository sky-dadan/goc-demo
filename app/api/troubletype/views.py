from app.api.routers import  router
from sqlalchemy.orm import  Session
from app.db.events import get_db
from fastapi import Depends
from app.api.troubletype.schema import TroubleTypeCreate
from app.models.models import TroubleType

import traceback


@router.get("/troubletype/hello")
async def hello():
    return "hello, troubletype"


@router.get("/troubletype/{troubletype_id}")
async def get_troubletype(troubletype_id:int, db: Session = Depends(get_db)):
    try:
        db_obj = db.query(TroubleType).filter_by(id=troubletype_id).first()
        return db_obj

    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.get("/troubletypes")
async def get_troubletypes(db: Session = Depends(get_db)):
    try:
        db_objs = db.query(TroubleType).all()
        return db_objs
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.post("/troubletype")
async def create_troubletype(item: TroubleTypeCreate, db: Session = Depends(get_db)):
    try:
        db_obj = db.query(TroubleType).filter_by(name=item.name).first()
        if db_obj:
            return {"code":200, "msg":"troubletype已存在"}
        db_obj = TroubleType(name=item.name)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}
