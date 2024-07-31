from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practice.models.book import Book, Base
from datetime import datetime

class BookManagement:
    def __init__(self, connection_string='sqlite:///:memory:', echo=True):
        self.engine = create_engine(connection_string, echo=echo)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_book(self, title, author, publication_date):
        if isinstance(publication_date, str):
            publication_date = datetime.strptime(publication_date, "%Y-%m-%d").date()
        new_book = Book(title=title, author=author, publication_date=publication_date)
        self.session.add(new_book)
        self.session.commit()

    def get_all_books(self):
        return self.session.query(Book).all()

    def close(self):
        self.session.close()
