#!/usr/bin/env python3
"""Hash password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a hashed password"""
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
