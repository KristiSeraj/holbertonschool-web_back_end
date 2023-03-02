#!/usr/bin/env python3
"""Basic babel app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@app.route('/')
def hello():
    """Return template 0-index.html which has hello world as h1"""
    return render_template('3-index.html', title=gettext("home_title"), header=gettext("home_header"))


@babel.localeselector
def get_locale():
    """Determine the best match for languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
