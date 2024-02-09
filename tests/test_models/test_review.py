#!/usr/bin/python3
import unittest
import pep8
import os
from models.review import Review
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set a Module"""
    pass


def tearDownModule():
    """ Function to remove a Module"""
    pass


class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        reviewFile = "models/review.py"
        test_reviewFile = "tests/test_models/test_review.py"
        check = style.check_files([reviewFile, test_reviewFile])
        self.assertEqual(check.total_errors, 0,
                         "Found code style has errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.review_test = Review()
        self.review_test.user_id = "bnb209"
        print("setUp")

    def tearDown(self):
        """ clean up a variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ set up a class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ clean up the class """
        print("tearDownClass")

    def userTest(self):
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def review_existTest(self):
        """ check if the methods exist """
        self.review_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.review_test, "__init__"))
        self.assertTrue(hasattr(self.review_test, "text"))
        self.assertTrue(hasattr(self.review_test, "user_id"))
        self.assertTrue(hasattr(self.review_test, "place_id"))

    def models_to_dictTest(self):
        model_dict = self.review_test.to_dict()
        self.assertIsInstance(model_dict["user_id"], str)
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def user_instanceTest(self):
        """ check if review is instance of Review """
        self.assertIsInstance(self.review_test, Review)

if __name__ == '__main__':
    unittest.main()
