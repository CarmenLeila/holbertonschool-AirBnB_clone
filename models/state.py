#!/usr/bin/python3
""" Creates a class of State """

from models.base_model import BaseModel


class State(BaseModel):
    """ 
    State class
    Args:
        BaseModel : inheritance
    """
    name = str("")
