#!/usr/bin/python3
import unittest
import pep8
import os
from models.state import State
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
        stateFile = "models/state.py"
        test_stateFile = "tests/test_models/test_state.py"
        check = style.check_files([stateFile, test_stateFile])
        self.assertEqual(check.total_errors, 0,
                         "Found code style has errors (warning).")


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

    def amenityTest(self):
        """ Check the documentation """
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def stateTest(self):
        """ check if the state methods exist """
        self.state_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.state_test, "__init__"))
        self.assertTrue(hasattr(self.state_test, "name"))

    def amenityNameTest(self):
        """ check if the name is create """
        self.state_test.name = 'Best'
        self.assertEqual(self.state_test.name, 'Best')

    def modelsToDictTest(self):
        model_dict = self.state_file.to_dict()
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def amenityInstanceTest(self):
        """ check if state is instance of State """
        self.assertIsInstance(self.state_test, State)

if __name__ == '__main__':
    unittest.main()
