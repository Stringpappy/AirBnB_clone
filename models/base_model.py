#!/usr/bin/python3
"""implementation of the class base model"""
import uuid
from datetime import datetime



class BaseModel:
    """super class"""

    def __init__(self):
        """initialising"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
<<<<<<< HEAD
        return "[{}] ({}) {}\
                ".format(self.__class__.__name__,  self.id, self.__dict__)
=======
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
>>>>>>> c50db0987b293791bd6180b4b52be8332e04d625

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        stuff_in_dict = self.__dict__.copy()
        stuff_in_dict['__class__'] = self.__class__.__name__
        stuff_in_dict['created_at'] = self.created_at.isoformat()
        stuff_in_dict['updated_at'] = self.updated_at.isoformat()
        return stuff_in_dict
