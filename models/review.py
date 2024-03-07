#!/usr/bin/python3
""" Creates a Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ 
    Review class
    Args:
        BaseModel : inheritance
    """
    place_id = str("")
    user_id = str("")
    text = str("")
