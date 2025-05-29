#lib/models/part.py
from sqlalchemy import Column, Integer, String

from . import Base

class Part(Base):
    
    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    quantity = Column(Integer)
   
    @classmethod
    def create(cls, session, name, description, quantity):
        part = cls(name=name, description=description,quantity=quantity)
        session.add(part)
        session.commit()
        return part

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def delete(cls, session, id):
        part = cls.find_by_id(session, id)
        if part:
            session.delete(part)
            session.commit()
            return True
        return False