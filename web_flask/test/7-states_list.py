#!/usr/bin/python3
"""
This module implements a simple Flask web application.
"""
from flask import Flask, render_template
from models.state import State
from models import storage
# Create a Flask application instance
app = Flask(__name__)


# Decorate the entry point route
@app.route("/states_list", strict_slashes=False)
def list_state():
    """
    Handle requests to the root URL ("/states_list")
    aand fetches the state stored in the dictionary or database.

    Returns:
    - html: A html that "
    """
    # This is a call to the get all the state object
    # store in the self.__objects{} dictionary or database
    # to retrive there values
    state_object = storage.all(State).values()
    # Store the return values in a list []
    state_object = list(state_object)
    # using a lambda function to arrange the state in
    # ascending order
    state_object.sort(key=lambda obj: obj.name)
    # store the sorted list in a dictionary
    dict_obj = {"states": state_object, "title": "HBNB",
                "header_title": "States"}

    return render_template("7-states_list.html", **dict_obj)


@app.teardown_appcontext
def flask_teardown(exception):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == "__main__":
    # Run the Flask application on host "0.0.0.0" and port 5000
    app.run(host="0.0.0.0", port='5000', debug=True)
