#!/usr/bin/python3
from models import base_model
import json

class FileStorage:
	__file_path = 'file.json'
	__objects = {}

	def all(self):
		return self.__objects

	def new(self, obj):
		key = f'{obj.__class__.__name__}.{obj.id}'
		self.__objects[key] = obj

	def  save(self):
		with open(self.__file_path, 'w', encoding='UTF-8') as file:
			data = {k : v.to_dict() for k, v in self.__objects.items()}
			json.dump(data, file)

	def reload(self):
		try:
			with open(self.__file_path, 'r', encoding='utf-8') as file:
				dict_obj = json.load(file)
				for val in dict_obj.values():
					class_name = val["__class__"]
					del val["__class__"]
					self.new(eval(f"base_model.{class_name}")(**val))
		except FileNotFoundError:
			return
