#!/usr/bin/python3
""" FileStorage class """

from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..place import Place
from ..amenity import Amenity
from ..review import Review
import json
import os


class FileStorage:
    """ class to process and convert classes to json file"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ initializes objects """
        pass

    def all(self):
        """ returns all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ creates a new instance """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """ serializes instances """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict.update({key: value.to_dict()})
        json_file = json.dumps(new_dict)
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json_file)

    def classesReload(self):
        """ Returns a dictionary of valid classes and their references """
        classes = {"BaseModel": BaseModel, "User": User,
                         "State": State, "City": City,
                         "Amenity": Amenity, "Place": Place,
                         "Review": Review}
        return classes

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
