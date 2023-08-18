"""Welcome Flask application."""

from flask import Flask


app = Flask(__name__)


@app.route('/welcome')
def say_welcome():
    """Return simple "welcome" Greeting."""

    msg = "welcome"
    return msg


@app.route('/welcome/home')
def say_welcome_home():
    """Return simple "welcome home" Greeting."""

    msg = "welcome home"
    return msg


@app.route('/welcome/back')
def say_welcome_back():
    """Return simple "welcome home" Greeting."""

    msg = "welcome back"
    return msg