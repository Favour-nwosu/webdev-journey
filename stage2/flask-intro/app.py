from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    conn = sqlite3.connect('posts.db')
    posts = conn.execute(
        "SELECT id , title , body, author FROM posts").fetchall()
    conn.close()
    return render_template("index.html", username="Favour", posts=posts)


@app.route("/about")
def about():
    return "what is the about page"


@app.route("/new-post", methods=["POST"])
def new_post():
    title = request.form["title"]
    body = request.form["body"]
    conn = sqlite3.connect('posts.db')
    conn.execute(
        "INSERT INTO posts (title, body, author) VALUES (?,?,?)", (title,
                                                                   body, "Favour")
    )
    conn.commit()
    conn.close()
    return redirect(url_for("home"))
