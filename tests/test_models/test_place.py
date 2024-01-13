#!/usr/bin/python3
"""unittests for base Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBase_PLace(unittest.TestCase):
    """unittests for base Place"""

    def test_type(self):
        self.assertEqual(Place, type(Place()))

    def test_is_instance(self):
        self.assertIsInstance(Place(), BaseModel)

    def test_id_type(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_instance_in_objects(self):
        self.assertIn(Place(), storage.all().values())

    def test_ids(self):
        cy1 = Place()
        cy2 = Place()
        self.assertNotEqual(cy1.id, cy2.id)


if __name__ == "__main__":
    unittest.main()
