#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User
import logging


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        logging.disable(logging.INFO)
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        logging.disable(logging.INFO)
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds user to the session
        """
        logging.disable(logging.INFO)
        usr = User(email=email, hashed_password=hashed_password)
        self._session.add(usr)
        self._session.commit()
        return usr

    def find_user_by(self, **kwargs) -> User:
        """
        Returns the first row found in users table filtered by input
        """
        logging.disable(logging.INFO)
        result = self._session.query(User).filter_by(**kwargs).first()
        if result is None:
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Locates the user to update and updates the user attributes
        """
        finded_user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            for i in range(len(dir(finded_user))):
                if dir(finded_user)[i] == k:
                    attr = dir(finded_user)[i]
                    finded_user.attr = v
                    return
            else:
                raise ValueError
