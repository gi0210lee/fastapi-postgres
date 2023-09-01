from database import Base
from sqlalchemy import Column, String, Boolean, Integer

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True, index=True, autoincrement=True)
    name = Column(String)