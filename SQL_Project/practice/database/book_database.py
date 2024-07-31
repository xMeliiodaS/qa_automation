from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practice.models.book import Book
from practice.models.base import Base


class BookDatabase:
    def __init__(self, connection_string='sqlite:///:memory:', echo=True):
        self.engine = create_engine(connection_string, echo=echo)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_book(self, title, author, publication_data):
        new_book = Book(title=title, author=author, publication_data=publication_data)
        self.session.add(new_book)
        self.session.commit()

    def get_all_books(self):
        return self.session.query(Book).all()

    def close(self):
        self.session.close()
