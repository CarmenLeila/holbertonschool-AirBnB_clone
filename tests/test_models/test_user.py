#!/usr/bin/python3
""" Unittest for User """

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def tearDown(self):
        """Tear down test environment"""
        del self.user

    def test_instance_creation(self):
        """Test if instance of User is created"""
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test attributes initialization"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')
