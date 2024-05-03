#!/usr/bin/python
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel, Base):
    """Representation of Review """
    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
