#!/usr/bin/env python3
"""Auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hashed password"""
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a uuid
    """
    return uuid.uuid4()


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user if user doesn't exist
        """
        try:
            usr = self._db.find_user_by(email=email)
            if usr:
                raise ValueError(f'User {usr.email} already exists')
        except NoResultFound:
            pwd = _hash_password(password)
            new_usr = self._db.add_user(email, pwd)
            return new_usr

    def valid_login(self, email: str, password: str) -> bool:
        """Validates the login
        """
        try:
            usr = self._db.find_user_by(email=email)
            if usr:
                return bcrypt.checkpw(bytes(password, 'utf-8'),
                                      usr.hashed_password)
        except NoResultFound:
            return False
