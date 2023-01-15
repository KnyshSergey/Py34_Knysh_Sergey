import sqlite3

database = sqlite3.connect('../database.db')

with open('posts.sql') as f:
    database.executescript(f.read())

cur = database.cursor()

cur.execute("INSERT INTO posts (username, password, content) VALUES (?, ?, ?)",
            ("User1", "123456", "My homework works!"))
cur.execute("INSERT INTO posts (username, password, content) VALUES (?, ?, ?)",
            ("User2", "67890", "My homework works too!"))

database.commit()

database.close()