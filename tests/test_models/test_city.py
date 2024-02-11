#!/usr/bin/python3

import unittest
import pep8
import os
from models.city import City
from models.engine.file_storage import FileStorage


def setUpModule():
    """It is a function to set a module"""

    pass


def tearDownModule():
    """ It is a function to delete a module"""

    pass

class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/city.py"
        file2 = "tests/test_models/test_city.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

class TestModels(unittest.TestCase):
    """It is a function to test the BaseModel."""

    def setUp(self):
        """This sets a variable."""

        self.city_1 = City()
        self.city_1.state_id = "100"
        print("setUp")

    def tearDown(self):
        """This ends variable."""

        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """This defines class."""

        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """This closes the class."""

        print("tearDownClass")

    def cityDocumetationTest(self):
        """This checks the documentation."""

        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def cityExistTest(self):
        """This checks if the city methods exists."""

        self.city_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.city_test, "__init__"))
        self.assertTrue(hasattr(self.city_test, "state_id"))
        self.assertTrue(hasattr(self.city_test, "name"))

    def cityNameTest(self):
        """This checks if the name is created."""

        self.city_test.name = 'Paris'
        self.assertEqual(self.city_test.name, 'Paris')

    def modelsToDictTest(self):

        model_dict = self.city_test.to_dict()
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertIsInstance(model_dict["state_id"], str)
        self.assertIsInstance(model_dict["id"], str)

    def cityInstanceTest(self):
        """This checks if city_test is instance of City."""
        self.assertIsInstance(self.city_test, City)


if __name__ == '__main__':
    unittest.main()
