#!/usr/bin/python3
''' Starts up Flask web app with routing '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def sHello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def sHbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def sCText(text):
    txt = text.replace('_', ' ')
    return "c {}".format(txt)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def sPythonText(text='is cool'):
    text = text.replace('_', ' ')
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
