import sqlite3

database = sqlite3.connect('../database.db')

with open('posts.sql') as f:
    database.executescript(f.read())

cur = database.cursor()

cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ("Sergey", "My Post", "It works"))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ("Andrey", "My Cars", "I have BMW!"))

database.commit()

database.close()