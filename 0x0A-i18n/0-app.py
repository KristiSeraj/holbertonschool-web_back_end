#!/usr/bin/env python3
"""Basic app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """Return template 0-index.html which has hello world as h1"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
