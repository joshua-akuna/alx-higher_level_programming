#!/usr/bin/python3
"""the test_base module contains all unit tests for the base module"""
import unittest
import json
import pep8
from models.base import Base


class Test_Base(unittest.TestCase):
    """ contains all unittests for the models/base.py module """
    def test_pep8_base(self):
        """ pep8 validation  """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_nb_objects_id(self):
        """ Test for the Base class id """
        base_obj = Base()
        self.assertEqual(base_obj.id, 1)

        base_obj = Base(None)
        self.assertEqual(base_obj.id, 2)

    def test_positive_id(self):
        """Test for positive Base class id"""
        base_obj = Base(14)
        self.assertEqual(base_obj.id, 14)

        base_obj = Base(21)
        self.assertEqual(base_obj.id, 21)

    def test_negative_id(self):
        """Test for negative Base class id"""
        base_obj = Base(-16)
        self.assertEqual(base_obj.id, -16)

        base_obj = Base(-9)
        self.assertEqual(base_obj.id, -9)

    def test_json_string_to_file(self):
        """ tests for the save_to_file function of the Base class """
        # this is an empty list
        empty_arr = []
        empty_json = json.dumps(empty_arr)
        # test for None parameter
        rect_dict_1 = None
        rect_json = Base.save_to_file(rect_dict_1)

        # self.assertEqual(rect_json, empty_json)

    def to_json_string(self):
        """tests for the to_json_string method of the Base class"""
        self.assertEqual(Base.to_json_string(None), '[]')

        empty_arr = []
        self.assertEqual(Base.to_json_string(empty_arr), '[]')
