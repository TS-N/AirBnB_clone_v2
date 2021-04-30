#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    @classmethod
    def setUpClass(cls):
        """
        set up for test
        """
        cls.review = Review()

    @classmethod
    def teardown(cls):
        """
        The end of the test
        """
        del cls.amenity

    def test_attr(self):
        """
        Test for the attribute
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
