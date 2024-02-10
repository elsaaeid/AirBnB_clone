#!/usr/bin/python3
import unittest
import pep8
import os
from models.user import User
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set up a Module"""
    pass


def tearDownModule():
    """ Function to clean up a Module"""
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
        """ Clean up variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set up class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Clean up the class """
        print("tearDownClass")

    def userTest(self):
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def userExistTest(self):
        """ Check if the user was created """
        self.user_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_test, "__init__"))
        self.assertTrue(hasattr(self.user_test, "first_name"))
        self.assertTrue(hasattr(self.user_test, "last_name"))
        self.assertTrue(hasattr(self.user_test, "email"))
        self.assertTrue(hasattr(self.user_test, "password"))

    def userFirstNameTest(self):
        """ Check if the firstname was created """
        self.assertEqual(self.user_test.firstname, 'Said')

    def userLastNameTest(self):
        """ Check if the lastname was created """
        self.assertEqual(self.user_test.lastname, "Ellithy")

    def userEmailTest(self):
        """ Check if the email was created """
        self.assertEqual(self.user_test.email, 'saidsadaoy@gmail.com')

    def userPasswordTest(self):
        """ Check if the password was created """
        self.assertEqual(self.user_test.password, "root")

    def modelsToDictTest(self):
        model_dict = self.user_test.to_dict()
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["email"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def userInstanceTest(self):
        """ check if user is instance of User """
        self.assertIsInstance(self.user_test, User)

if __name__ == '__main__':
    unittest.main()
