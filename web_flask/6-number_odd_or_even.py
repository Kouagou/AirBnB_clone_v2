#!/usr/bin/python3
""" A script that starts a Flask web application. """
from markupsafe import escape
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_(text):
    """Display C followed by <text>. """
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_is_(text="is cool"):
    """Display Python followed by <text>. """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display <n> is a number if true. """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    """Display <n> is a number if true. """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    """Display <n> is odd or even. """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
