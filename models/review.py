#!/usr/bin/python3
"""
class Review inherits from Basemodel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review with three attributes"""
    place_id = ""
    user_id = ""
    text = ""
