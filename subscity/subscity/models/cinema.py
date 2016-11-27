from datetime import datetime
from pymysql.err import IntegrityError
import json

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    String,
    Integer,
    Text,
)

from subscity.models.meta import Base, DBSession


class Cinema(Base):
    __tablename__ = 'cinemas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    api_id = Column(String(64), nullable=False)
    city_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
    metro = Column(String(255), nullable=True)
    url = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=True)
    fetch_all = Column(Boolean(name='fetch_all'), default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now,
                        nullable=False)

    @staticmethod
    def get_all():
        return DBSession.query(Cinema).all()

    def save(self):
        try:
            DBSession.add(self)
            DBSession.commit()
        except:
            DBSession.rollback()
            raise

    def as_json(self):
        return json.dumps(self.__dict__)
