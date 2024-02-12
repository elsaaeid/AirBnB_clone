#!/usr/bin/python3
import unittest
import os
from models.review import Review
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set a Module"""
    pass


def tearDownModule():
    """ Function to delete a Module"""
    pass


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set up a variable """
        self.review_test = Review()
        self.review_test.user_id = "asd123"
        print("setUp")

    def tearDown(self):
        """ Clean variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set up class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Clean the class """
        print("tearDownClass")

    def reviewTest(self):
        """ Check the review """
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def reviewExistTest(self):
        """ Check if the methods exist """
        self.review_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.review_test, "__init__"))
        self.assertTrue(hasattr(self.review_test, "text"))
        self.assertTrue(hasattr(self.review_test, "user_id"))
        self.assertTrue(hasattr(self.review_test, "place_id"))

    def modelsToDictTest(self):
        """ Check the converting to dict """
        my_dict = self.review_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["user_id"], str)
        self.assertIsInstance(my_dict["id"], str)

    def reviewInstanceTest(self):
        """ Check if review_test is instance of Review """
        self.assertIsInstance(self.review_test, Review)

if __name__ == '__main__':
    unittest.main()
