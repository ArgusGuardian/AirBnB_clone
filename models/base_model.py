#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = created_at_iso
        dic['updated_at'] = updated_at_iso
        return dic

