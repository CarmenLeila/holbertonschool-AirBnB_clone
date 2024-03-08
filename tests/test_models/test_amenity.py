#!/usr/bin/python3
""" Unittest for Amenity """

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_instance_creation(self):
        """Test if instance of Amenity is created"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name_attribute(self):
        """Test the name attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, '')
