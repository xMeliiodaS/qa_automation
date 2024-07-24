import sqlite3

conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

cur.execute("DELETE from users")
name = "Bahaa"
age = 30
cur.execute("INSERT INTO users (name ,age) VALUES (?, ?)", (name, age))

# Fetching data with a parameter
cur.execute("SELECT * FROM users WHERE age > ?", (29,))
rows = cur.fetchall()
for row in rows:
    print(row)
