import sqlite3
from with_yair.school_task.table import Table

conn = sqlite3.connect('schoolDB.db')

# Create a cursor object
cur = conn.cursor()

# Delete the table
cur.execute('DROP TABLE students')

# Create the table
Table().create_table(cur)

# Insert students into the table
Table().insert_into_table(cur, '1234', 'Bahaa', '77')
Table().insert_into_table(cur, '4561', 'Shibel', '97')
Table().insert_into_table(cur, '7891', 'Majd', '92')
Table().insert_into_table(cur, '2281', 'Joseph', '100')

# Commit the transactions
conn.commit()

# Query students with grades greater than 80, sorted by grade in descending order
cur.execute("SELECT * FROM students WHERE student_grade > ? ORDER BY student_grade DESC", (80,))

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
