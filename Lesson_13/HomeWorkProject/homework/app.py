import sqlite3

from flask import Flask, render_template
import sqlite3

def get_db_connection():
    database = sqlite3.connect("database.db")
    database.row_factory = sqlite3.Row
    return database


app = Flask(__name__)

@app.route('/')
def index():
    database = get_db_connection()
    posts = database.execute("SELECT * FROM posts").fetchall()
    return render_template("index.html", posts=posts)

@app.route('/create')
def create():
    return render_template("newPost.html")

if __name__ == '__main__':
    app.run(debug=True)

