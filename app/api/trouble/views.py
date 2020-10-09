from app.api.routers import router
from app.models.models import Trouble
from app.api.trouble import schema
from app.db.events import connection_db

import traceback
import time

db = connection_db()
@router.get("/trouble/{trouble_id}")
async def read_troulbe(trouble_id: int):
    try:
        trouble_obj = db.query(Trouble).filter_by(id=trouble_id).first()
        result = trouble_obj.item_to_json()
        result['department_name'] = trouble_obj.department.name
        result['troubletype_name'] = trouble_obj.troubletype.name
        return {"code":200, "data": result}

    except:
        print(traceback.format_exc())
        return {"code":500, "msg": traceback.format_exc()}


@router.get('/troubles')
async def get_troubles():
    try:
        trouble_objs = db.query(Trouble).all()
        result = []
        for trouble_obj in trouble_objs:
            tmp = trouble_obj.item_to_json()
            tmp['department_name'] = trouble_obj.department.name
            tmp['troubletype_name'] = trouble_obj.troubletype.name
            result.append(tmp)
            print(result)
        return {"code":200, "data": result}
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.put("/trouble")
async def update_trouble():
    try:
        trouble_obj = db.query(Trouble).filter_by(id=1).first()
        print(Trouble.item_to_json(trouble_obj))
        trouble_obj.title = "xiaodu"
        trouble_obj.department_id = 2
        db.commit()
        db.flush()
        db.refresh(trouble_obj)
        return trouble_obj
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}


@router.post("/trouble")
async def create_trouble(item: schema.TroubleCreate):
    try:
        db_trouble = Trouble(department_id=item.department_id, troubletype_id=item.troubletype_id,title=item.title,
                             createtime=time.strftime("%Y-%m-%d %H:%M:%S"))
        db.add(db_trouble)
        db.commit()
        db.refresh(db_trouble)
        return db_trouble
    except:
        print(traceback.format_exc())
        return {"code": 500, "msg": traceback.format_exc()}

