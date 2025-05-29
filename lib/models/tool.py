from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Tool(Base):

    __tablename__ = 'tools'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    checkouts = relationship("Checkout", back_populates="tool")

    @classmethod
    def create(cls, session, name, description):
        tool = cls(name=name, description=description)
        session.add(tool)
        session.commit()
        return tool

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
        
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def delete(cls, session, id):
        tool = cls.find_by_id(session, id)
        if tool:
                session.delete(tool)
                session.commit()
                return True
        return False
        

