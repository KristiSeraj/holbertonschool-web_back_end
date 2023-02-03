#!/usr/bin/env python3
"""Hash password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a hashed password"""
    return bcrypt.hashpw(b"{password}", bcrypt.gensalt())
