import pathlib

from flask import Flask

app = Flask(__name__)
here = pathlib.Path(__file__).parent.absolute()


@app.route("/")
def hello():
    return "Hello, Cleveland!!!"


@app.route("/favicon.ico")
def favicon():
    with open(here / 'favicon.ico', 'rb') as inf:
        return inf.read()
