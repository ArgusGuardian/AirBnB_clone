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

    def test_city_id_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_str(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_is_str(self):
        self.assertEqual(str, type(Place.name))

    def test_description_str(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_int(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_int(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_int(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_int(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_float(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_float(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_list(self):
        self.assertEqual(list, type(Place.amenity_ids))


if __name__ == "__main__":
    unittest.main()
