#!/usr/bin/python3
''' Starts Flask web app, renders HTML containing all States '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def removeSession(exception):
    '''Removes the current SQLAlchemy Session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def allStates():
    '''Shows all State instances'''
    states = storage.all('State')
    return render_template('7-states_list.html', state=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
