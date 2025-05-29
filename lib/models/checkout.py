#lib/models/checkout.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class Checkout(Base):
    __tablename__ = 'checkouts'
    
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('users.id'))
    tool_id = Column(Integer, ForeignKey('tools.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="checkouts")
    tool = relationship("Tool", back_populates="checkouts")
    @classmethod
    def create(cls, session, user_id, tool_id):
        checkout= cls(user_id=user_id, tool_id=tool_id)
        session.add(checkout)
        session.commit()
        return checkout

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def delete(cls, session, id):
        checkout = cls.find_by_id(session, id)
        if checkout:
            session.delete(checkout)
            session.commit()
            return True
        return False

