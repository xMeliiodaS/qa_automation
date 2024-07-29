class Table:

    @staticmethod
    def create_table(cur):
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT,
                student_grade INTEGER
            )'''
        )

    @staticmethod
    def insert_into_table(cur, student_id, name, grade):
        cur.execute("INSERT INTO students (student_id, student_name, student_grade) VALUES (?, ?, ?)",
                    (student_id, name, grade))

    @staticmethod
    def delete_student(cur, student_id):
        cur.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
