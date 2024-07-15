#!/usr/bin/python3
"""modules Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ fubc Review class that inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
