from flask import Flask

# Creating app object
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"
