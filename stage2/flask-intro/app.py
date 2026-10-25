from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    posts = [
        {"title": "first post", "author": "favour",
            "body": "this is the first post."},
        {"title": "second post", "author": "Alice",
            "body": "this is the second post"},
        {"title": "third post", "author": "Bob",
            "body": "this is the third post."}
    ]

    return render_template("index.html", username="Favour", posts=posts)


@app.route("/about")
def about():
    return "what is the about page"


if __name__ == "__main__":
    app.run(debug=True)
