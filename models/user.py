#!/usr/bin/python3
""" Creation of User """

from models.base_model import BaseModel

class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a User instance"""
        super().__init__(*args, **kwargs)
