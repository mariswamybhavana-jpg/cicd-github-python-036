from flask import Flask

app = Flask(__name__)


def add_numbers(a, b):
    return a + b


@app.route("/")
def home():
    return "CI/CD Pipeline Application is Running"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(add_numbers(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)