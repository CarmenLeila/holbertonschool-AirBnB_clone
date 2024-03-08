#!/usr/bin/python3
""" Defines FileStorage class """
# file_storage.py

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON """

    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Add new object in __objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        json_object = {}
        """ fill dictionary with elements __objects """
        for key, value in self.__objects.items():
            json_object[key] = value.to_dict()
        try:
            with open(self.__file_path, 'w' , encoding = 'utf-8') as file:
                json.dump(json_object, file, indent=4)
        except Exception:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects """
        if not os.path.exists(self.__file_path) or
            os.path.getsize(self.__file_path):
            return
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = key.split(".")[0]
                    instance = eval(class_name)(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
