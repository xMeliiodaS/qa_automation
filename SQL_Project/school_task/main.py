import sqlite3
from school_task.table import Table

conn = sqlite3.connect('schoolDB.db')

# Create a cursor object
cur = conn.cursor()

# Delete the table
cur.execute('DROP TABLE students')

# Create the table
Table().create_table(cur)

# Insert students into the table
Table().insert_into_table(cur, '1234', 'Bahaa', '99')
Table().insert_into_table(cur, '4561', 'Shibel', '79')
Table().insert_into_table(cur, '7891', 'Majd', '75')
Table().insert_into_table(cur, '2281', 'Joseph', '100')

# Commit the transactions
conn.commit()

cur.execute("SELECT * FROM students WHERE student_grade > 80")
rows = cur.fetchall()
for row in rows:
    print(row)
print()

Table().delete_student(cur, "2281")

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
cur.close()
conn.close()
