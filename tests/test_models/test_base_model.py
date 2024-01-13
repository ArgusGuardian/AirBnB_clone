import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBase_instantiation(unittest.TestCase):
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

    def test_cupdated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_instance_in_objects(self):
        self.assertIn(BaseModel(), storage.all().values())


if __name__ == "__main__":
    unittest.main()
