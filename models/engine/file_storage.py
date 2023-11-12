#!/usr/bin/python3
"""Module to control data storage"""

from models.base_model import BaseModel
import json
from models.user import User


class FileStorage:
    """Controls how objects are stored"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns all instances"""
        return self.__objects

    def new(self, obj):
        """Creates a new instance object"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Save object from memory in json file"""
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            data = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Retrieves from json file stored objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                dict_obj = json.load(file)
                for val in dict_obj.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(f"{class_name}")(**val))
        except FileNotFoundError:
            return
