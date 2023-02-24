#!/usr/bin/env python3
"""Basic babel app"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
