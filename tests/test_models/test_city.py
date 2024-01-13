#!/usr/bin/python3
"""unittests for base City"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBase_City(unittest.TestCase):
    """unittests for base City"""

    def test_type(self):
        self.assertEqual(City, type(City()))

    def test_is_instance(self):
        self.assertIsInstance(City(), BaseModel)

    def test_id_type(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_instance_in_objects(self):
        self.assertIn(City(), storage.all().values())

    def test_ids(self):
        a = City()
        b = City()
        self.assertNotEqual(a.id, b.id)


if __name__ == "__main__":
    unittest.main()
