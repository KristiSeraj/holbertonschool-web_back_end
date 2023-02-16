#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def hello():
    """Message to greet"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """Register a user"""
    if request.method == 'POST':
        usr_email = request.form['email']
        usr_pwd = request.form['password']
        try:
            usr = AUTH.register_user(usr_email, usr_pwd)
            if usr:
                return jsonify({"email": usr_email, "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'])
def login():
    """Login a user with session id"""
    if request.method == 'POST':
        usr_email = request.form['email']
        usr_password = request.form['password']
        usr = AUTH.valid_login(usr_email, usr_password)
        if not usr:
            abort(401)
        else:
            session_id = AUTH.create_session(usr_email)
            response = jsonify({"email": "<user email>",
                                "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logout a user with session id"""
    if request.method == 'DELETE':
        session_id = request.cookies.get('session_id')
        usr = AUTH.get_user_from_session_id(session_id)
        if usr:
            AUTH.destroy_session(usr.id)
            return redirect(url_for('/'))
        else:
            abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
