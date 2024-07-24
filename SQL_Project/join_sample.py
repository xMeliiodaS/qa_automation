import sqlite3

conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# cur.execute('DROP TABLE user')

# Execute SQL commands
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

conn.commit()
conn.close()
