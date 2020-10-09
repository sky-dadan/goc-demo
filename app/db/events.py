from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from app.core.config import MYSQL_HOST, MYSQL_PASSWD, MYSQL_PORT, MYSQL_USER

#链接mysqlURL配置
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/test".format(MYSQL_USER,MYSQL_PASSWD,
                                                                                            MYSQL_HOST,MYSQL_PORT)


Base = declarative_base()


def get_db():
    try:
        logger.info("Connection  to database")
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(bind=engine)
        db = SessionLocal()
        yield db
    finally:
        db.close()


def connection_db():
    try:
        logger.info("Connection  to database")
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(bind=engine)
        db = SessionLocal()
        return db
    finally:
        db.close()