#!/usr/bin/python3
""" A script that starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_states_list():
    """Display all states """
    #states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_resources(exception):
    """ A method to handle some stuff. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
