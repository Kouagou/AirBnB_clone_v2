#!/usr/bin/python3
""" A script that starts a Flask web application. """


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def get_states(state_id=None):
    """ Display the states and cities listed in alphabetical order. """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close_resources(exception):
    """ Closes the storage on teardown. """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
