from practice.database.book_database import BookDatabase


def main():
    db = BookDatabase()

    db.add_book('Bahaa', 'Shibel', "2")
    db.add_book('Shibel', "Majd", "2")

    students = db.get_all_books()

    for student in students:
        print(f"{student.name} is on grade {student.grade} and is id {student.id}")

    db.close()


if __name__ == "__main__":
    main()
