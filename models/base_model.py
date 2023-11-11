""" Module that defines a base model """
from datetime import datetime
import uuid
import models


class BaseModel:
    """ BaseModel for class """

    def __init__(self, *args, **kwargs) -> None:
        """ Initialize base_mdel class
            Arguments:
            args - objects
            kwargs - objects
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
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save obj to file """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a copy of dictionary containing
        all keys / values of __dict__ """
        my_dict_copy = self.__dict__.copy()
        my_dict_copy["__class__"] = self.__class__.__name__
        my_dict_copy["created_at"] = self.created_at.isoformat()
        my_dict_copy["updated_at"] = self.updated_at.isoformat()
        return my_dict_copy
