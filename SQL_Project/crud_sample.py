import sqlite3

conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# Insert
cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

print("Start")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# Update
cur.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
print("\nAfter update")
for row in rows:
    print(row)

# Delete
cur.execute("DELETE FROM users WHERE name = 'Bob'")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
print("\nAfter update")
for row in rows:
    print(row)

conn.commit()
conn.close()