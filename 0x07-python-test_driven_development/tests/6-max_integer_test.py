#!/usr/bin/python
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def text_doc_string(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def text_func_doc_string(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_args(self):
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, None])

        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)

    def test_single_element_list(self):
        self.assertEqual(max_integer([8]), 8)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 5, 7, 9]), 9)
        self.assertEqual(max_integer([1, 2, 5, 15, 9]), 15)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -5, -7, -9]), -1)
        self.assertEqual(max_integer([-21, -92, -85, -15, -19]), -15)


if __name__ == '__main__':
    unittest.main()
