#!/usr/bin/python3
''' Starts Flask web app, renders HTML containing all States '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def removeSession(response_or_exc):
    '''Removes the current SQLAlchemy Session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def allStates():
    '''Shows all State instances'''
    data = storage.all('State')
    states = []
    for key, value in data.items():
        states.append(value)
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
