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


if __name__ == "__main__":
    unittest.main()
