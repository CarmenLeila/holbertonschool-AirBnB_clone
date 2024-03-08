#!/usr/bin/python3
""" Unittest for BaseModel """

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down test environment"""
        del self.base_model

    def test_instance_creation(self):
        """Test if instance of BaseModel is created"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id_generation(self):
        """Test if ID is generated"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        """Test if created_at is datetime type"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at is datetime type"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test __str__ method"""
        string_representation = str(self.base_model)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)

    def test_save_method(self):
        """Test save method"""
        first_updated_at = self.base_model.updated_at
        self.base_model.save()
        second_updated_at = self.base_model.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)
        self.assertEqual(base_model_dict['id'], self.base_model.id)
