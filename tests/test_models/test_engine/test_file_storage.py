#!/usr/bin/python3
"""Unit tests for the FileStorage"""



import unittest
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for storage"""
    def setUp(self):        
        """ Set up test environment """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open('file.json', 'r') as file:
            self.assertIn(obj.id, file.read())

    def test_reload(self):
        base_model = BaseModel()
        user = User()
        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.save()

        self.storage._FileStorage__objects = {}
        self.storage.reload()

        base_model_key = "BaseModel." + base_model.id
        user_key = "User." + user.id
        self.assertIn(base_model_key, self.storage._FileStorage__objects)
        self.assertIn(user_key, self.storage._FileStorage__objects)

        os.remove(self.file_path)
        try:
            self.storage.reload()
        except FileNotFoundError:
            self.fail("FileNotFoundError was raised")

if __name__ == "__main__":
    unittest.main()