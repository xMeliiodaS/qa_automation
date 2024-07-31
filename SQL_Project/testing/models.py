from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    #   There is no init in the SQP table
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    email = Column(String)
