#!/usr/bin/python3
""" Module to handle JSON file """
import json
from os.path import isfile


class FileStorage:
    """ FileStorage class to handle JSON """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """ add in '__objects' a BaseModel instance dict info """
        FileStorage.__objects[obj.getType + "." + obj.id] = obj

    def save(self):
        """ serializes '__objects' to the JSON file """
        with open(FileStorage.__file_path, 'w', encoding='utf8') as f:
            json.dump({k: v.to_dict() for k, v
                       in FileStorage.__objects.items()}, f)

    # Create and list from JSON file

    def reload(self):
        """ Read a JSON file, create a respective BaseModel instances
        and store each one in '__objects' """
        if not isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r', encoding='utf8') as f:
            for v in json.load(f).values():
                self.new(self._create_obj(v['__class__'], v))

    @staticmethod
    def _create_obj(className, chargeValues):
        """ Create an instance from a class dynamically """
        from models.base_model import BaseModel
        return locals()[className](**chargeValues)
