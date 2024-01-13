#!/usr/bin/python3
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class Test_FileStorage(unittest.TestCase):
    def test_FileStorage_type(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_dict_type(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_type(self):
        self.assertEqual(type(storage), FileStorage)
    def test_class_type(self):
        self.assertEqual(type(FileStorage()), FileStorage)
    