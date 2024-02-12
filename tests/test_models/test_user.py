#!/usr/bin/python3
import unittest
import os
from models.user import User
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
        """ Set a variable """
        self.user_test = User()
        self.user_test.name = 'Said'
        self.user_test.lastname = "Ellithy"
        self.user_test.email = 'saidsadaoy@gmail.com'
        self.user_test.password = "root"
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ define class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ close the class """
        print("tearDownClass")

    def test_user(self):
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def place_cityTest(self):
        """ check if the city name is create """
        self.user_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_test, "__init__"))
        self.assertTrue(hasattr(self.user_test, "email"))
        self.assertTrue(hasattr(self.user_test, "password"))
        self.assertTrue(hasattr(self.user_test, "first_name"))
        self.assertTrue(hasattr(self.user_test, "last_name"))

    def user_nameTest(self):
        """ check if the name is create """
        self.assertEqual(self.user_test.name, 'Said')

    def user_lastnameTest(self):
        """ chaeck if the lastname is create """
        self.assertEqual(self.user_test.lastname, "Ellithy")

    def user_emailTest(self):
        """ chaeck if the email is create """
        self.assertEqual(self.user_test.email, 'saidsadaoy@gmail.com')

    def user_passwordTest(self):
        """ chaeck if the password is create """
        self.assertEqual(self.user_test.password, "root")

    def models_to_dictTest(self):
        my_dict = self.user_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["email"], str)
        self.assertIsInstance(my_dict["id"], str)

    def user_instanceTest(self):
        """ check if user_test is instance of User """
        self.assertIsInstance(self.user_test, User)

if __name__ == '__main__':
    unittest.main()
