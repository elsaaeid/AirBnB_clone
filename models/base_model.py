#!/usr/bin/python3
import json
import os
from datetime import datetime
import uuid
from hashlib import md5
import models


class BaseModel():
    """Base model that all classes will inherit from"""
    __abstract__ = True

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
        if 'password' in kwargs:
            self.password = md5(kwargs['password'].encode()).hexdigest()
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")

    def update(self, attribute_dict):
        """Update the instance with the
        provided attribute dictionary"""
        for key, value in attribute_dict.items():
            setattr(self, key, value)
        self.save()

    def __str__(self):
        """Returns the string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def to_dict(self):
        """Converts instance into dict format"""
        new_dict = self.__dict__.copy()
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        dT = datetime
        if "created_at" in new_dict and isinstance(new_dict["created_at"], dT):
            new_dict["created_at"] = new_dict["created_at"].strftime(format_t)
        if "updated_at" in new_dict and isinstance(new_dict["updated_at"], dT):
            new_dict["updated_at"] = new_dict["updated_at"].strftime(format_t)
        new_dict["__class__"] = type(self).__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    @classmethod
    def reload(cls):
        """Deserializes the JSON file to instances"""
        file_path = "file.json"
        format_created = datetime.strptime(obj_data['created_at'],
                                           "%Y-%m-%dT%H:%M:%S.%f")
        format_updated = datetime.strptime(obj_data['updated_at'],
                                           "%Y-%m-%dT%H:%M:%S.%f")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                for obj_id, obj_data in data.items():
                    if obj_data['__class__'] == cls.__name__:
                        del obj_data['__class__']
                        obj_data['created_at'] = format_created
                        obj_data['updated_at'] = format_updated
                        if 'password' in obj_data:
                            obj_data['password'] = md5(
                                obj_data['password'].encode()
                                ).hexdigest()
                        instance = cls(**obj_data)
                        setattr(cls, obj_id, instance)

    def save(self):
        """Updates the updated_at and serializes
        instances to a JSON file
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
