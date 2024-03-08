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
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_object, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_instance = self.supported_classes.get(class_name)
                    if class_instance:
                        instance = class_instance(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
