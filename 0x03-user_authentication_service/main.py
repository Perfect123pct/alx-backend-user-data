#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User
from auth import Auth

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))


my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated")
except ValueError:
    print("Error")

print(_hash_password("Hello Holberton"))

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

AUTH = Auth()

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "WrongPwd"))

print(auth.valid_login("unknown@email", password))

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))


"""
Main module to interact with the endpoints of the Flask application
"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register a new user"""
    url = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    print(f"User {email} successfully registered.")


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt to log in with the wrong password"""
    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 401
    print(f"Attempted to log in with the wrong password for user {email}.")


def log_in(email: str, password: str) -> str:
    """Log in with correct credentials and return the session ID"""
    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    session_id = response.json()["session_id"]
    print(f"User {email} successfully logged in. Session ID: {session_id}")
    return session_id


# Add functions for other tasks...


if __name__ == "__main__":
    EMAIL = "guillaume@holberton.io"
    PASSWD = "b4l0u"
    NEW_PASSWD = "t4rt1fl3tt3"

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    session_id = log_in(EMAIL, PASSWD)
    # Add calls to other functions...

