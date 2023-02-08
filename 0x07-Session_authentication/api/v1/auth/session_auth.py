#!/usr/bin/env python3
"""Session auth"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creating session"""
        if user_id is None or type(user_id) is not str:
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a session ID"""
        if session_id is None and type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)