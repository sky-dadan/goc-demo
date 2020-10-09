from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import  relationship
from app.db.events import Base

class BaseModel(Base):
    __abstract__ = True

    def item_to_json(obj):
        return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

    def items_to_json(all_objs):
        v = [obj.item_to_json() for obj in all_objs]
        return v



class Trouble(BaseModel):
    __tablename__ = "trouble"

    id = Column(Integer, primary_key=True, index=True)
    createtime = Column(DateTime)
    department_id = Column(Integer, ForeignKey("department.id"))
    troubletype_id = Column(Integer, ForeignKey("troubletype.id"))
    title = Column(String(100))
    department = relationship('Department', backref="trouble_of_department")
    troubletype = relationship('TroubleType',backref="trouble_of_type")

class TroubleType(BaseModel):
    __tablename__ = "troubletype"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))


class Department(BaseModel):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
