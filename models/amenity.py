#!/usr/bin/python3
"""Amenity Module

This Module inherits from BaseModel class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class

    Attributes:
        name (str): The Amenity name

    """
    name = ''
