#!/usr/bin/python3

"""This script shows the base model """

import uuid
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
        if kwargs is not None and kwargs != {}:
            for key, values in kwargs.items():
                if key == "id":
                    self.id = kwargs.get(key)
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
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
            """Returns a string representation of the instance"""
            cls = (str(type(self)).split('.')[-1]).split('\'')[0]
            return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

        def save(self):
            """updates the update_at"""
            self.updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            """Convert instance into dict format"""
            my_dict = {}
            my_dict.update(self.__dict__)
            my_dict.update({'__class__':
                            (str(type(self)).split('.')[-1]).split('\'')[0]})
            my_dict['created_at'] = self.created_at.isoformat()
            my_dict['updated_at'] = self.updated_at.isoformat()
            return my_dict
