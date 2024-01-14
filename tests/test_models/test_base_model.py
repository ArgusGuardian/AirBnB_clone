#!/usr/bin/python3
"""testing all cases for class BaseModel"""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from time import sleep
class TestBase_BaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class"""
    def test_id(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)
    def test_type(self):
        self.assertEqual(BaseModel, type(BaseModel()))
    def test_id_type(self):
        self.assertEqual(str, type(BaseModel().id))
    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))
    def test_updated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))
    def test_instance_in_objects(self):
        self.assertIn(BaseModel(), storage.all().values())
    def test_check_time_created_at(self):
        a = BaseModel()
        sleep(0.05)
        b = BaseModel()
        self.assertLess(a.created_at, b.created_at)
    def test_check_time_updated_at(self):
        a = BaseModel()
        sleep(0.05)
        b = BaseModel()
        self.assertLess(a.updated_at, b.updated_at)
    def test_args_unused(self):
        a = BaseModel(None)
        self.assertNotIn(None, a.__dict__.values())
    
    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)
    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())
    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)
    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)
    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))
    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

if __name__ == "__main__":
    unittest.main()
