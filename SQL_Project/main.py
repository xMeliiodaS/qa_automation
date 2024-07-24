import sqlite3

conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# Execute SQL commands
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# Delete the table
# cur.execute('DROP TABLE user')

conn.commit()
conn.close()
