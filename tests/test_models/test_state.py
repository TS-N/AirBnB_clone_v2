#!/usr/bin/python3
"""
Unittest for the State class that inherit from BaseModel
"""
import unittest
from models.state import State
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel


class TestState(test_basemodel):
    """
    Tests for the State class
    """
    def setUp(self):
        """
        To define instructions that will be executed before each test
        """
        self.my_state = State()

    def test_instance(self):
        """
        Test the instance of the class
        """
        self.assertIsInstance(self.my_state, State)

    def test_inheritence(self):
        """
        Test if the class inherit from BaseModel
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attr(self):
        """
        Test the attributes
        """
        self.assertTrue(hasattr(self.my_state, 'id'))
        self.assertTrue(hasattr(self.my_state, 'created_at'))
        self.assertTrue(hasattr(self.my_state, 'updated_at'))
        self.assertTrue(hasattr(self.my_state, 'name'))

    def test_name_type(self):
        """
        Test the type of the attribute name
        """
        self.my_state.name = "Colorado"
        self.assertIsInstance(self.my_state.name, str)

    def test_set_name(self):
        """
        Test to set the name
        """
        self.my_state.name = "Colorado"
        self.assertEqual(self.my_state.name, "Colorado")

    def tearDown(self):
        """
        To define instructions that will be executed after each test
        """
        del self.my_state
