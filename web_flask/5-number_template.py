#!/usr/bin/python3
"""
This module implements a simple Flask web application.
"""
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Decorate the entry point route
@app.route("/", strict_slashes=False)
def entry():
    """
    Handle requests to the root URL ("/").

    Returns:
    - str: A greeting message, "Hello HBNB!"
    """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def holborton():
    """
    Handle request to the holborton URL

    Returns:
    - str: Holborton Abreviation, "HBNB"
    """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cvairable(text):
    """
    Handle request with variable

    Returns:
    - str: C + string passed
    """
    formated_text = text.replace('_', ' ')

    return 'C {}'.format(formated_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>')
def pythonvairable(text="is cool"):
    """
    Handle requests to the Python variable path

    Returns:
    - str: Python + string entered
    """
    formated_text = text.replace('_', ' ')

    return 'Python {}'.format(formated_text)


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """
    Handle url requests to /number/int

    Returns:
    - str: number passed through the url and a str
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def sendInteger(n):
    """
    Handles incomming request on /number_template/<number>

    Returns:
    - html: a html page
    """
    ctxt = {'number': n, 'title': "HBNB"}
    return render_template("5-number.html",
                           **ctxt)


if __name__ == "__main__":
    # Run the Flask application on host "0.0.0.0" and port 5000
    app.run(host="0.0.0.0", port='5000')
