from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", username="Favour", message_count=5)


@app.route("/about")
def about():
    return "what is the about page"


if __name__ == "__main__":
    app.run(debug=True)
