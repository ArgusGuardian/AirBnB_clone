#!/usr/bin/python3
"""
unittests for base Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBase_Review(unittest.TestCase):
    """unittests for base Review"""

    def test_type(self):
        self.assertEqual(Review, type(Review()))

    def test_is_instance(self):
        self.assertIsInstance(Review(), BaseModel)

    def test_id_type(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_instance_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_ids(self):
        a = Review()
        b = Review()
        self.assertNotEqual(a.id, b.id)

    def test_place_id_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_str(self):
        self.assertEqual(str, type(Review.text))


if __name__ == "__main__":
    unittest.main()
