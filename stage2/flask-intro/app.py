from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask is running"


@app.route("/about")
def about():
    return "what is the about page"


if __name__ == "__main__":
    app.run(debug=True)
