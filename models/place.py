#!/usr/bin/python
"""Place class"""
import models
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """Representation of Place """

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """Returns the list of Review instances"""
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """Returns the list of Amenity instances"""
        amenity_list = []
        all_amenities = models.storage.all(Amenity)
        for amenity in all_amenities.values():
            if amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list
