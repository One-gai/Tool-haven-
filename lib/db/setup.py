from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

engine = create_engine('sqlite:///inventory.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)
