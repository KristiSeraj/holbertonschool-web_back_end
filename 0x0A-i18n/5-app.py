#!/usr/bin/env python3
"""Basic babel app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


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
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """Determine the best match for languages"""
    if 'locale' in request.args and\
            request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user from request"""
    try:
        usr_id = request.args['login_as']
        return users[int(usr_id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """Execute get user method before any request"""
    g.user = get_user()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
