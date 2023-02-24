#!/usr/bin/env python3
"""Basic babel app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@app.route('/')
def hello():
    """Return template 0-index.html which has hello world as h1"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
