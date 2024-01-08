#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key,value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.__dict__[key] = datetime.strptime(value, date_format)
                elif key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value

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

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)