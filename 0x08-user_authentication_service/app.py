#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request, make_response
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
        if usr:
            session_id = AUTH.create_session(usr_email)
            response = make_response('Setting cookie')
            response.set_cookie('session_id', session_id)
            return jsonify({'email': usr_email, 'message': 'logged in'})
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
