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
        """ Set up a variable """
        self.user_test = User()
        self.user_test.name = 'Said'
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

    def placeCityTest(self):
        """ Check if the city name is create """
        self.user_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_test, "__init__"))
        self.assertTrue(hasattr(self.user_test, "email"))
        self.assertTrue(hasattr(self.user_test, "password"))
        self.assertTrue(hasattr(self.user_test, "first_name"))
        self.assertTrue(hasattr(self.user_test, "last_name"))

    def userNameTest(self):
        """ Check if the name is create """
        self.assertEqual(self.user_test.name, 'Said')

    def userLastnameTest(self):
        """ Chaeck if the lastname is create """
        self.assertEqual(self.user_test.lastname, "Ellithy")

    def userEmailTest(self):
        """ Chaeck if the email is create """
        self.assertEqual(self.user_test.email, 'saidsadaoy@gmail.com')

    def userPasswordTest(self):
        """ Chaeck if the password is create """
        self.assertEqual(self.user_test.password, "root")

    def modelsToDictTest(self):
        """ Check the converting to dict """
        my_dict = self.user_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["email"], str)
        self.assertIsInstance(my_dict["id"], str)

    def userInstanceTest(self):
        """ Check if user_test is instance of User """
        self.assertIsInstance(self.user_test, User)

if __name__ == '__main__':
    unittest.main()
