#!/usr/bin/python3
"""the test_base module contains all unit tests for the base module"""
import unittest
import json
import pep8
from models.base import Base


class Test_Base(unittest.TestCase):
    """  """
    def test_pep8_base(self):
        """  """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_json_string_to_file(self):
        """  """
        # this is an empty list
        empty_arr = []
        empty_json = json.dumps(ampty_arr)
        # test for None parameter
        rect_dict_1 = None
        rect_json = Base.save_to_file(rect_dict_1)

        self.assertEqual(rect_json, empty_json)

