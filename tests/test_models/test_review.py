#!/usr/bin/python3
import unittest
import os
import pep8
from models.review import Review
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set up a Module"""
    pass


def tearDownModule():
    """ Function to clean up a Module"""
    pass

class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/review.py"
        file2 = "tests/test_models/test_review.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set up a variable """
        self.review_test = Review()
        self.review_test.user_id = "bnb209"
        print("setUp")

    def tearDown(self):
        """ Clean up a variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set up a class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Clean up the class """
        print("tearDownClass")

    def userTest(self):
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
        """ Check if models converted to dictionary """
        model_dict = self.review_test.to_dict()
        self.assertIsInstance(model_dict["user_id"], str)
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def userInstanceTest(self):
        """ Check if review is instance of Review """
        self.assertIsInstance(self.review_test, Review)


if __name__ == '__main__':
    unittest.main()
