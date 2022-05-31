import time
from datetime import datetime

import schedule
import sqlalchemy as db
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('mysql://user:password@127.0.0.1:3306/database')
# engine = db.create_engine(
#     'mysql://cpldev:cpldevdeptrai202X@cpl-dev2.cxihrjsldwdw.ap-southeast-1.rds.amazonaws.com:3306/bitcastle')
connection = engine.connect()
session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)()


Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    time = Column(Integer)


Base.metadata.create_all(bind=engine)


def producer():
    record = UserModel()
    record.time = int(time.time())
    session.add(record)
    session.commit()
    print("Added record: {}".format(datetime.fromtimestamp(record.time)))


if __name__ == "__main__":
    schedule.every(1).second.do(producer)

    while True:
        schedule.run_pending()
        time.sleep(1)
