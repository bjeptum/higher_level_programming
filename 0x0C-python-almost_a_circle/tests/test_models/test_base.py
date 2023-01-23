#!/usr/bin/python3
"""Test Cases for the Base Module"""


import unittest
import inspect
import pep8
import json


from models.base import Base


class TestBaseDocs(unittest.TestCase):
    """Veriffies Base module documentation"""
    @classmethod
    def setUpClass(cls):
        """Set the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def pep8_test(self):
        """Check compliance to PEP8 and documentation"""
        style = pep8.StyleGuide(quiet=True)
        style.options.max_line_length = 100
        check = style.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0,
                         'PEP8 style errors: %d' % check.total_errors)


class TestBase(unittest.TestCase):
    """Working of the Base Class"""
    def test_id_none(self):
        """Test id as None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """Test id"""
        b89 = Base(89)
        self.assertEqual(b89.id, 89)

    def test_no_id_after_set(self):
        """Test id as None"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb_private(self):
        """Tests nb_objects as a private instance attribute"""
        b = Base(3)
        with self.asserRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b._nb_objects)

    def test_to_json_string(self):
        """Tests simple to json string"""
        Base._Base__nb_objects = 0
        d1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        d2 = {"x": 3, "width": 9, "id": 2, "height": 6, "y": 7}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_to_json_string_empty(self):
        """Test an empty list"""
        json.s = BAse.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_to_json_string_None(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)self.assertEqual(json_s, "[]")
