#!/user/bin/python3

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestModels(unittest.TestCase):
    """ This is a unittests of testing instantiation of BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Initialize to basemodel test """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Set up a variable """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def testDefaultValue(self):
        """ Check defualt values """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def testKwargs(self):
        """ Check kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def testKwargsValue(self):
        """ Check kwargs value """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def modelsSaveTest(self):
        """ This checks if the save function works """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def testString(self):
        """ Check string """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def modelsToDictTest(self):
        """ test the to_dict method of the BaseModel class """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def testId(self):
        """ Check id type"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def testCreatedAt(self):
        """ Check created_at datetime"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def testUpdatedAt(self):
        """ Check updated_at datetime """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
