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
    return str(uuid.uuid4())


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
        except NoResultFound:
            pwd = _hash_password(password)
            new_usr = self._db.add_user(email, pwd)
            return new_usr
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Validates the login
        """
        try:
            usr = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(bytes(password, 'utf-8'),
                                  usr.hashed_password)

    def create_session(self, email: str) -> str:
        """Creates a session
        """
        try:
            usr = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            usr_id = _generate_uuid()
            self._db.update_user(usr.id, session_id=usr_id)
            return usr_id

    def get_user_from_session_id(self, session_id: str) -> User or None:
        """Get users based on session id
        """
        try:
            usr = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return usr

    def destroy_session(self, user_id: int) -> None:
        """Destroy session
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates reset password token
        """
        try:
            usr = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        rst_token = _generate_uuid()
        self._db.update_user(usr.id, reset_token=rst_token)
        return rst_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password based on reset token
        """
        try:
            usr = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        pwd = _hash_password(password)
        self._db.update_user(usr.id, hashed_password=pwd, reset_token=None)
