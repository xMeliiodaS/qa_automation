from practice.database.book_management import BookManagement
from datetime import datetime


def main():
    db = BookManagement()

    # Add books with publication dates
    db.add_book('Bahaa', 'Shibel', "2024-01-01")
    db.add_book('Shibel', 'Majd', "2024-02-02")

    books = db.get_all_books()

    for book in books:
        print(f"{book.title} by {book.author}, published on {book.publication_date}, ID {book.id}")

    db.close()


if __name__ == "__main__":
    main()
