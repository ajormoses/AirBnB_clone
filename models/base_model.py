#!/usr/bin/python3
""" Base Model Module """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Base Model Class """

    def __init__(self, *args, **kwargs) -> None:
        """
        Init Method

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeFormat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with current datetime

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns dictionary containing all keys/values """
        class_details = self.__dict__.copy()
        class_details['__class__'] = self.__class__.__name__
        class_details['created_at'] = self.created_at.isoformat()
        class_details['updated_at'] = self.updated_at.isoformat()

        return class_details
