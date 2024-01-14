#!/usr/bin/python3
"""unittests for base State"""
import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBase_State(unittest.TestCase):
    """unittests for base State"""

    def test_type(self):
        self.assertEqual(State, type(State()))

    def test_is_instance(self):
        self.assertIsInstance(State(), BaseModel)

    def test_id_type(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_instance_in_objects(self):
        self.assertIn(State(), storage.all().values())

    def test_ids(self):
        a = State()
        b = State()
        self.assertNotEqual(a.id, b.id)

    def test_email_is_public_str(self):
        self.assertEqual(str, type(State.name))


if __name__ == "__main__":
    unittest.main()
