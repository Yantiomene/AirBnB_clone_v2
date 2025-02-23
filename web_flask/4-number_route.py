#!/usr/bin/python3
""" File to start a Flask web application """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """function  to render the route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Serve the hbnb page"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """Serve the C page with text argument"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/<text>")
@app.route("/python")
def python(text="is cool"):
    """Serve the python route"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """Serve a number"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
