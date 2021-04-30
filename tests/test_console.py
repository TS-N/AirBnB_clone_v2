#!/usr/bin/python3
"""Test for the console"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City


class TestConsole(unittest.TestCase):
    """
    Tests for the console
    """
    @classmethod
    def setUpClass(cls):
        """
        A class method called before tests in an individual class run
        """
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        A class method called after tests in an individual class have run
        """
        del cls.console

    def test_create(self):
        """
        Test create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create hello")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create Amenity name="Wifi"')

    def test_quit(self):
        """
        test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_emptyline(self):
        """
        Test empty line
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_all(self):
        """
        Test all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Hello")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all City")
            self.assertEqual("{}\n", f.getvalue())

    def test_show(self):
        """
        Test show command inpout
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Hello")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
