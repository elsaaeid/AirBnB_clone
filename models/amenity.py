#!/usr/bin/python
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity """
    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
