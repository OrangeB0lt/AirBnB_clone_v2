#!/usr/bin/python3
''' Starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    ''' Closes curr SQLAlchemy session after request '''
    storage.close()


@app.route('/states_list')
def stateLists():
    ''' Injects states and info into html '''
    states = storage.all('State')
    return render_template('7-states_list.html', state=states)


@app.route('/cities_by_states')
def cityLists():
    ''' Injects the cities into html '''
    states = storage.all('State')
    return render_template('8-cities_by_states.html', state=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
