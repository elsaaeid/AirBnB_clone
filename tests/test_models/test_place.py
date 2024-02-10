#!/usr/bin/python3
import unittest
import pep8
import os
from models.place import Place
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
        placeFile = "models/place.py"
        test_placeFile = "tests/test_models/test_place.py"
        check = style.check_files([placeFile,test_placeFile ])
        self.assertEqual(check.total_errors, 0,
                         "Found code style has errors (warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set up a variable """
        self.place_test = Place()
        self.place_test.number_bathrooms = 1
        self.place_test.longitude = 10.10
        print("setUp")

    def tearDown(self):
        """ clean up variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ set up the class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ cleanup the class """
        print("tearDownClass")

    def placeTest(self):
        """ check documentation """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def CityExistTest(self):
        """ check if the city name is create """
        self.place_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.place_test, "__init__"))
        self.assertTrue(hasattr(self.place_test, "city_id"))
        self.assertTrue(hasattr(self.place_test, "user_id"))
        self.assertTrue(hasattr(self.place_test, "name"))
        self.assertTrue(hasattr(self.place_test, "description"))
        self.assertTrue(hasattr(self.place_test, "number_rooms"))
        self.assertTrue(hasattr(self.place_test, "number_bathrooms"))
        self.assertTrue(hasattr(self.place_test, "max_guest"))
        self.assertTrue(hasattr(self.place_test, "price_by_night"))
        self.assertTrue(hasattr(self.place_test, "latitude"))
        self.assertTrue(hasattr(self.place_test, "longitude"))
        self.assertTrue(hasattr(self.place_test, "amenity_ids"))

    def modelsToDictTest(self)
        models_dict = self.place_test.to_dict()
        self.assertIsInstance(models_dict["id"], str)
        self.assertIsInstance(models_dict["created_at"], str)
        self.assertIsInstance(models_dict["updated_at"], str)
        self.assertIsInstance(models_dict["number_bathrooms"], int)
        self.assertIsInstance(models_dict["longitude"], float)

    def placeIsInstanceTest(self):
        """ check if place is instance of Place """
        self.assertIsInstance(self.place_test, Place)


if __name__ == '__main__':
    unittest.main()
