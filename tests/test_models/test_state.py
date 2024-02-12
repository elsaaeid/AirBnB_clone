#!/usr/bin/python3
import unittest
import os
from models.state import State


def setUpModule():
    """ Funtion to set up a Module"""
    pass


def tearDownModule():
    """ Function to clean up a Module"""
    pass


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set up a variable """
        self.state_test = State()
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

    def stateTest(self):
        """ Check the documentation """
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def stateExistTest(self):
        """ Check if the state methods exist """
        self.state_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.state_test, "__init__"))
        self.assertTrue(hasattr(self.state_test, "name"))

    def stateNameTest(self):
        """ Check if the state name was created """
        self.state_test.name = 'Best'
        self.assertEqual(self.state_test.name, 'Best')

    def modelsToDictTest(self):
        """ Check if models converted to dictionary """
        my_dict = self.state_file.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)

    def stateInstanceTest(self):
        """ Check if state is instance of State """
        self.assertIsInstance(self.state_test, State)


if __name__ == '__main__':
    unittest.main()
