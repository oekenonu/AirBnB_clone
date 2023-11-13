#!/usr/bin/python3
"""Module that defines a BaseModel class"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """ BaseModel for class """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize base_model class

        Args:
            *args - not used
            **kwargs - key value pairs representing attributes
        """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """Return string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update time with current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a copy of dictionary containing
        all keys / values of __dict__
        """
        my_dict_copy = self.__dict__.copy()
        my_dict_copy["__class__"] = self.__class__.__name__
        my_dict_copy["created_at"] = self.created_at.isoformat()
        my_dict_copy["updated_at"] = self.updated_at.isoformat()
        return my_dict_copy
