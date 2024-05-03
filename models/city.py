#!/usr/bin/python
"""city class"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of city """
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
