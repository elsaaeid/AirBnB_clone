#!/usr/bin/python3

"""This script shows the base model"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """This is basemodel for AirBnB project and all classes
                                     will inherit from it"""
    def __init__(self, *args, **kwargs):
        """This is initialization of instance attributes.
            *args: this is a list of arguments
            **kwargs: this is a dict of key-values arguments
        """
        if len(kwargs) != 0:
            for key, values in kwargs.items():
                if key == "id":
                    self.id = kwargs.get(key)
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "my_number":
                    self.my_number = kwargs.get(key)

                elif key == "name":
                    self.name = kwargs.get(key)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new = (self)

        def __str__(self):
            """returns string representation"""
            return ("[{}] ({}) {}".format(self.__class__.__name__,
                                          self.id, self.__dict__))

        def save(self):
            """updates the update_at"""
            self.updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            """returns a dictionary which contain all keys and values
                                                        of ___dict__"""
            my_dict = self.__dict__.copy()
            my_dict['created_at'] = self.created_at.isoformat()
            my_dict['updated_at'] = self.updated_at.isoformat()
            my_dict['__class__'] = self.__class__.__name__
            return (my_dict)
