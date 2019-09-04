#!/usr/bin/python3
''' Starts Flask web app with routing '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def sHello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def sHbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def sCText(text):
    text = text.replace('_', ' ')
    return "c {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def sPythonText(text='is cool'):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def shNumber(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numTemplate(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numOddEven(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
