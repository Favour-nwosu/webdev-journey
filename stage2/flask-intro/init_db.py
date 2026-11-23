import sqlite3

conn = sqlite3.connect('posts.db')
conn.execute(""" 
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL
 )
""")

conn.execute(""" 
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    author TEXT NOT NULL
    )
""")
conn.commit()
conn.close()
print("table created")
