#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods for other classes
"""
from models import storage
import uuid
import datetime


class BaseModel:
    """superclass"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.datetime.strptime(value,\
                                "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = self.created_at
        storage.save()

    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = type(self).__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
