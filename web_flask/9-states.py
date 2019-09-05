#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


def getStateList():
    '''gets dict of states from storage'''
    storage.reload()
    return [[v.id, v.name] for v in storage.all("State").values()]


@app.route('/states', strict_slashes=False)
def statesList():
    '''list all the states'''
    states = get_state_list()
    return render_template('9-states.html', states=states, cities=None)


@app.route('/states/<id>', strict_slashes=False)
def cityById(id=None):
    '''list cities and states by id'''
    states = get_state_list()
    state = None
    for num in states:
        if num[0] == id:
            state = num[1]
    if state is None:
        return render_template('9-states.html', states=None)
    citiesdict = storage.all("City")
    cities = []
    for _, v in citiesdict.items():
        if v.state_id == id:
            cities.append([v.id, v.name])
    return render_template('9-states.html',
                           states=state,
                           cities=cities)


@app.teardown_appcontext
def close(exception):
    '''tear down the database'''
    storage.close()


if __name__ == '__main__':
    app.run()
