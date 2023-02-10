#!/usr/bin/env python3
""" Module of Session auth views
"""
from flask import jsonify, request, session
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Login request"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email:
            return jsonify({"error": "email missing"}), 400
        if not password:
            return jsonify({"error": "password missing"}), 400
        usr = User.search({'email': email})
        if not usr:
            return jsonify({"error": "no user found for this email"}), 404
        for u in usr:
            if not u.is_valid_password(password):
                return jsonify({"error": "wrong password"}), 401
            from api.v1.app import auth
            session_id = auth.create_session(u.id)
            response = jsonify(u.to_json())
            response.set_cookie(os.environ.get('SESSION_NAME'), session_id)
            return response
