#!/usr/bin/python3
"""

"""
import uuid
from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    
    """
    def test_base_model_id_is_string(self):
        """
        
        """
        bMod = BaseModel()
        self.assertIsInstance(bMod.id, str)

    def test_base_model_created_at_is_datetime(self):
        """
        
        """
        bMod = BaseModel()
        self.assertIsInstance(bMod.created_at, datetime)
        
    def test_base_model_updated_at_is_datetime(self):
        """
        
        """
        bMod = BaseModel()
        self.assertIsInstance(bMod.updated_at, datetime)

    def test_base_model_uuid_expected_format(self):
        """
        
        """
        bMod = BaseModel()
        self.assertIsInstance(uuid.UUID(bMod.id), uuid.UUID)

    # def test_base_model_uuid_wrong_format(self):
    #     """
        
    #     """
    #     bMod = BaseModel()

    def test_base_model_uuid_version(self):
        """
        
        """
        bMod = BaseModel()
        converted_uuid = uuid.UUID(bMod.id)

        self.assertEqual(converted_uuid.version, 4)

    def test_base_model_different_uuid(self):
        """
        
        """
        bMod_one = BaseModel()
        bMod_two = BaseModel()
        converted_uuid_one = uuid.UUID(bMod_one.id)
        converted_uuid_two = uuid.UUID(bMod_two.id)

        self.assertNotEqual(converted_uuid_one, converted_uuid_two)
