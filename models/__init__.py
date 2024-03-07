#!/usr/bin/python3
""" Defines all common attributes/methods """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Storage

storage = FileStorage()
storage.reload()

# Models classes

classes = [
    "BaseModel",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
]

# Attributs types

int_attrs = [
    "number_rooms",
    "number_bathrooms",
    "max_guest",
    "price_by_night"
]

float_attrs = [
    "latitude",
    "longitude"
]
