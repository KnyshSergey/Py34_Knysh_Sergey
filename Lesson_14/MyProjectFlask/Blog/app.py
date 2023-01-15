import sqlite3

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

def get_db_connection():
    database = sqlite3.connect("database.db")
    database.row_factory = sqlite3.Row
    return database

def getpost(id):
    database = get_db_connection()
    post = database.execute("SELECT * FROM posts Where id = ?", (id,)).fetchone()
    return post



app = Flask(__name__)

@app.route('/')
def index():
    database = get_db_connection()
    posts = database.execute("SELECT * FROM posts ORDER BY posts.created DESC").fetchall()
    return render_template("index.html", posts=posts)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template("newPost.html")
    elif request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']
        database = get_db_connection()
        database.execute('INSERT INTO posts (author, title, content) VALUES (?, ?, ?)', (author, title, content))
        database.commit()
        database.close()

        return redirect(url_for('index'))


@app.route('/post-<int:id>/')
def post(id):
    post = getpost(id)
    return render_template('postDetail.html', post=post)

@app.route('/delete/post-<int:id>/', methods=['POST'])
def delete_post(id):
    database = get_db_connection()
    database.execute("DELETE FROM posts Where id = ?", (id,))
    database.commit()
    database.close()
    return redirect(url_for('index'))

@app.route('/', methods=['POST'])
def delete_all():
        database = get_db_connection()
        database.execute("DELETE FROM posts WHERE id >= 1")
        database.commit()
        database.close()
        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

