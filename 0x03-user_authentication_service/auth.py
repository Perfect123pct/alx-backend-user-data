#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from user import User

from sqlalchemy.orm.exc import NoResultFound
from bcrypt import hashpw, gensalt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Check if login credentials are valid
        """
        try:
            user = self._db.find_user_by(email=email)
            return self._check_password(password, user.hashed_password)
        except NoResultFound:
            return False

    def _hash_password(self, password: str) -> bytes:
        """Hash the password using bcrypt
        """
        return hashpw(password.encode('utf-8'), gensalt())

    def _check_password(self, password: str, hashed_password: str) -> bool:
        """Check if the password matches the hashed password
        """
        return hashpw(password.encode('utf-8'), hashed_password.encode('utf-8')) == hashed_password

    def create_session(self, email: str) -> str:
        """Create a new session for the user
        """
        user = self._db.find_user_by(email=email)
        session_id = self._generate_uuid()
        user.session_id = session_id
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    # Implement other methods as required

    def _generate_uuid(self) -> str:
        """Generate a new UUID
        """
        # Implement UUID generation
        pass

