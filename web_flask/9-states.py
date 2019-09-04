#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def removeSession(response_or_exc):
    ''' Removes the current SQLAlchemy Session '''
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def showStateCities(state_id=None):
    ''' Shows State and its Cities, or all States if no id is passed in '''
    data = storage.all('State')
    states = []
    target = None
    for key, value in data.items():
        states.append(value)
        if state_id == value.id:
            target = value

    return render_template('9-states.html', states=states,
                           target=target, state_id=state_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
