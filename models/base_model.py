#!/usr/bin/python3
"""module base_model that all other classes will inherit from"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """class BaseModel that defines all common
    attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initialize attributes for class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, date_format)
                elif key != '__class__':
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = created_at_iso
        dic['updated_at'] = updated_at_iso
        return dic

    def __str__(self):
        """print the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
