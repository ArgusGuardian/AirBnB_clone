#!/usr/bin/python3
"""
unittests for base Amenity
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBase_Amenity(unittest.TestCase):
    """unittests for base Amenity"""

    def test_type(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_is_instance(self):
        self.assertIsInstance(Amenity(), BaseModel)

    def test_id_type(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_instance_in_objects(self):
        self.assertIn(Amenity(), storage.all().values())

    def test_ids(self):
        a = Amenity()
        b = Amenity()
        self.assertNotEqual(a.id, b.id)

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Amenity.name))


if __name__ == "__main__":
    unittest.main()
