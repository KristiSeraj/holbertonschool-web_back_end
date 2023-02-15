#!/usr/bin/env python3
"""Auth module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashed password"""
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
