#!/usr/bin/python3
"""User class"""
import models
from models.base_model import BaseModel
import hashlib


class User(BaseModel):
    """Representation of a user """
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """sets user pasword"""
        if key == "password":
            value = hashlib.md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
