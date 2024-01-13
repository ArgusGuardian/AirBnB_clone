#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBase_State(unittest.TestCase):
    def test_type(self):
        self.assertEqual(User, type(User()))

    def test_is_instance(self):
        self.assertIsInstance(User(), BaseModel)

    def test_id_type(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_instance_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_ids(self):
        a = User()
        b = User()
        self.assertNotEqual(a.id, b.id)

if __name__ == "__main__":
    unittest.main()
