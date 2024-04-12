#!/usr/bin/env python3
"""
encrypt_password module
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)

