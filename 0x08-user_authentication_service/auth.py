#!/usr/bin/env python3
"""Auth module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashed password"""
    pwd = b"{password}"
    hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())
    return hashed
