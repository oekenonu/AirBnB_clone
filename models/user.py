#!/usr/bin/python3
"""Module to manage Users"""
from models import base_model


class User(base_model.BaseModel):
    """User class to manage user attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
