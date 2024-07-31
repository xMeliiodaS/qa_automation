from sqlalchemy import Column, Integer, String, Float

from practice.models.base import Base


class Book(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(Float)
    publication_data = Column(String)
