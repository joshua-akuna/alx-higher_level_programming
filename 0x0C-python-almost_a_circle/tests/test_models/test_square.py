#!/usr/bin/python3
"""This module defines the TestSquare class"""
import unittest
import pep8
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """This class is a unittest for the square module and Square class"""

    def test_pep8_square(self):
        """pep8 validation"""
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def is_rect_subclass(self):
        """checks that the Square class is a sub class of Rectangle"""
        self.assertTrues(issubclass(Square, Rectangle))

    def test_square_init(self):
        """test the initialization Square class"""
        s1 = Square(5)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 5)

        s2 = Square(4, 7, 2, 19)
        self.assertEqual(s2.id, 19)
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.x, 7)
        self.assertEqual(s2.y, 2)

    def test_none_integer_size_param(self):
        with self.assertRaises(TypeError) as err:
            Square("size")

    def test_no_param_initialization(self):
        with self.assertRaises(TypeError) as err:
            Square("size")
        
        with self.assertRaises(TypeError) as err:
            Square(True)
        
        with self.assertRaises(TypeError) as err:
            Square(10.5)

    def test_zero_negative_param_init(self):
        with self.assertRaises(ValueError) as err:
            Square(0)

        with self.assertRaises(ValueError) as err:
            Square(-12)

    def test_square_area(self):
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)

    def test_square_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 15
        self.assertEqual(s1.size, 15)

        with self.assertRaises(TypeError) as err:
            s1.size = "20"

        with self.assertRaises(ValueError) as err:
            s1.size = -5
