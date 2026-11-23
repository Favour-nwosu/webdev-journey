from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "dev-secret-change-this-later"


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        conn = sqlite3.connect("posts.db")
        conn.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?,?,?)", (username, email,
                                                                                  password_hash)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = sqlite3.connect("posts.db")
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        conn.close()
        if user and bcrypt.checkpw(password.encode(), user[3]):
            session["user_username"] = user[1]
            return redirect(url_for("home"))
        return "invaild credential", 401
    return render_template("login.html")


@app.route("/")
def home():
    conn = sqlite3.connect('posts.db')
    posts = conn.execute(
        "SELECT id , title , body, author FROM posts").fetchall()
    conn.close()
    return render_template("index.html", username=session.get("user_username", ""), posts=posts)


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
                                                                   body, session.get("user_username"))
    )
    conn.commit()
    conn.close()
    return redirect(url_for("home"))
