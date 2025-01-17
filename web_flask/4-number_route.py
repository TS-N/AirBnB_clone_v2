#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ routed function """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ routed function """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ routed function """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def textPy(text):
    """ routed function """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:number>', strict_slashes=False)
def print_number(number):
    """ routed function """
    return ("{:d} is a number".format(number))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
