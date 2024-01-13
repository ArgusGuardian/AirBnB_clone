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


if __name__ == "__main__":
    unittest.main()
