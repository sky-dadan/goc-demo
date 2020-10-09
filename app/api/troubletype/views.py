from app.api.routers import  router
from app.db.events import connection_db
from app.api.troubletype.schema import TroubleTypeCreate
from app.models.models import TroubleType

import traceback

db = connection_db()

@router.get("/troubletype/hello")
async def hello():
    return "hello, troubletype"


@router.get("/troubletype/{troubletype_id}")
async def get_troubletype(troubletype_id:int):
    try:
        db_obj = db.query(TroubleType).filter_by(id=troubletype_id).first()
        return {"code":200, "data":db_obj}

    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.get("/troubletypes")
async def get_troubletypes():
    try:
        db_objs = db.query(TroubleType).all()
        return {"code":200, "data":db_objs}
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.post("/troubletype")
async def create_troubletype(item: TroubleTypeCreate):
    try:
        db_obj = db.query(TroubleType).filter_by(name=item.name).first()
        if db_obj:
            return {"code":200, "msg":"troubletype已存在"}
        db_obj = TroubleType(name=item.name)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return {"code":200, "data":db_obj}
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}
