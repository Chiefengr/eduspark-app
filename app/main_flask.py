# app/main_flask.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to EduSpark Flask App"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
