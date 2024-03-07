#!/usr/bin/python3
""" Creation of City """

from models.base_model import BaseModel


class City(BaseModel):
    """ 
    City class
    Args:
        BaseModel : inheritance
    """
    state_id = str("")
    name = str("")
