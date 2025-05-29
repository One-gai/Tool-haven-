from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

    checkouts = relationship("Checkout", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', role='{self.role}')>"


    @classmethod
    def create(cls, session, name, role):
        user = cls(name=name, role=role)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def delete(cls, session, id):
        user = cls.find_by_id(session, id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
