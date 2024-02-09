#!/usr/bin/python3
import unittest
import pep8
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel


def setUpModule():
    """ """
    pass


def tearDownModule():
    """ """
    pass


class TestString(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        storageModule = "models/engine/file_storage.py"
        matchingModule = "tests/test_models/test_engine/test_file_storage.py"
        check = style.check_files([storageModule, matchingModule])
        self.assertEqual(check.total_errors, 0,
                         "Found code style has errors (warning).")


class TestModels(unittest.TestCase):

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.file_storage = FileStorage()
        print("setUp")

    def tearDown(self):
        """ Clean up after test cases """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Clean a Class"""
        print("tearDownClass")

    def file_storageTest(self):
        """ Check the documentation of file storage """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def file_storage_existTest(self):
        """ Check if methods exist """
        self.assertTrue(hasattr(self.file_storage, "__init__"))
        self.assertTrue(hasattr(self.file_storage, "all"))
        self.assertTrue(hasattr(self.file_storage, "new"))
        self.assertTrue(hasattr(self.file_storage, "save"))
        self.assertTrue(hasattr(self.file_storage, "reload"))

    def models_saveTest(self):
        """ Check if the save of function works """
        self.my_model.name = "Hello"
        self.my_model.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Hello")
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)

if __name__ == '__main__':
    unittest.main()
