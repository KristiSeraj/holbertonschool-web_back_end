#!/usr/bin/env python3
"""API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Path required"""
        if path is None or excluded_paths is None or excluded_paths is []:
            return True
        if path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """Header authorization"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return current user"""
        return None
