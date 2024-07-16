#!/usr/bin/python3
""" 
module that serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ construct """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        x = FileStorage.__objects
        return x

    def new(self, obj):
        """ func sets in dictionary the obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ func that serializes objectss to the JSON file """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            nw_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(nw_dict, fname)

    def reload(self):
        """ func that Reload the file """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as name_of_file:
                jsonf = json.load(name_of_file)
                for key, val in jsonf.items():
                    FileStorage.__objects[key] = eval(
                        val['__class__'])(**val)
