#!/usr/bin/python3
""" Unit tests for the FileStorage """

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
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all() method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test new() method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertIsNotNone(objects.get(key))

    def test_save_reload(self):
        """Test save() and reload() methods"""
        # Create and save some models
        model1 = BaseModel()
        model2 = Amenity()
        model3 = City()
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.new(model3)
        self.storage.save()

        # Instantiate another FileStorage to reload
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        objects = new_storage.all()
        # Check if objects were reloaded correctly
        self.assertIn("BaseModel." + model1.id, objects)
        self.assertIn("Amenity." + model2.id, objects)
        self.assertIn("City." + model3.id, objects)
