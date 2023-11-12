#!/usr/bin/python3
"""Module for Reviewes"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents reviews"""

    place_id = ""
    user_id = ""
    text = ""
