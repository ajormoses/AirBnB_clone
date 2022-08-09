#!/usr/bin/python3
""" State Class """

from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits BaseModel

    Attributes:
        name (str): The name of the state.
    """
    name = ""
