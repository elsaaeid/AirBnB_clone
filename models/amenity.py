#!/usr/bin/python3

"""amenity class"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """this is amenity clas"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
