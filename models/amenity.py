#!/usr/bin/python3
""" Creation of Amenity """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class
    Args:
        BaseModel : inheritance
    """
    name = str("")
