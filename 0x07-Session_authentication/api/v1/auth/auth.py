#!/usr/bin/env python3
"""API authentication"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Path required"""
        if path is None or excluded_paths is None or excluded_paths is []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        if path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """Header authorization"""
        if request is None:
            return None
        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return current user"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None
        my_session_id = os.environ.get('SESSION_NAME')
        return request.cookies.get(my_session_id)
