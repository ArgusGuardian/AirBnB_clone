#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage():
    __file_path = "file.json"
    __objects = {}
     
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                object_stored= json.load(f)
                for o in object_stored.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

