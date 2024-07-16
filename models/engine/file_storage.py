import json
"""recreate a BaseModel from another one by using a dictionary rep"""


class FileStorage:
    __file_path = "file.json"
    __object = {}

    def all(self):
        """  returns the dictionary """
        return self.__object

    def new(self, obj):
        """set in key"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__object[key] = obj

    def save(self):
        """Serializaation of the JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserialization"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_to_serialized = json.load(f)
                for key, obj_dict in obj_to_serialized.items():
                    cls_name, obj_id = key.split('.')
                    m = __import__('models.' + cls_name, fromlist=[cls_name])
                    cls = getattr(m, cls_name)
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

        def attributes(self):
        """Returns the valid attributes and their types for classname."""
        my_attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return my_attributes
