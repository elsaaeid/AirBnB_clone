#!/usr/bin/python3
import unittest
import pep8
import os
from models.user import User
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set a Module"""
    pass


def tearDownModule():
    """ Function to delete a Module"""
    pass


class TestString(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        userFile = "models/user.py"
        test_userFile = "tests/test_models/test_user.py"
        check = style.check_files([userFile, test_userFile])
        self.assertEqual(check.total_errors, 0,
                         "Found code style has errors (warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set up a variable """
        self.user_test = User()
        self.user_test.firstname = 'Said'
        self.user_test.lastname = "Ellithy"
        self.user_test.email = 'saidsadaoy@gmail.com'
        self.user_test.password = "root"
        print("setUp")

    def tearDown(self):
        """ clean up variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ set up class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ clean up the class """
        print("tearDownClass")

    def userTest(self):
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def place_cityTest(self):
        """ check if the city name is create """
        self.user_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_test, "__init__"))
        self.assertTrue(hasattr(self.user_test, "first_name"))
        self.assertTrue(hasattr(self.user_test, "last_name"))
        self.assertTrue(hasattr(self.user_test, "email"))
        self.assertTrue(hasattr(self.user_test, "password"))

    def user_firstNameTest(self):
        """ check if the name is create """
        self.assertEqual(self.user_test.firstname, 'Said')

    def user_lastNameTest(self):
        """ chaeck if the lastname is create """
        self.assertEqual(self.user_test.lastname, "Ellithy")

    def user_emailTest(self):
        """ chaeck if the email is create """
        self.assertEqual(self.user_test.email, 'saidsadaoy@gmail.com')

    def user_passwordTest(self):
        """ chaeck if the password is create """
        self.assertEqual(self.user_test.password, "root")

    def models_to_dictTest(self):
        model_dict = self.user_test.to_dict()
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["email"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def user_instanceTest(self):
        """ check if user is instance of User """
        self.assertIsInstance(self.user_test, User)

if __name__ == '__main__':
    unittest.main()
