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
        """test the initialization of Square instances with valid integers
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_square_init_with_2_args(self):
        """test the initialization of Square instances with valid integers
        """
        s1 = Square(1, 2)
        self.assertEqual(s1.size, 1)

    def test_square_init_with_3_args(self):
        """test the initialization of Square instances with valid integers
        """
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_square_init_with_4_args(self):
        """test the initialization of Square instances with valid integers
        """
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, 4)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_square_init_with_invalid_size_arg(self):
        """test the initialization of Square instances with invalid
        non integer argument
        """
        with self.assertRaises(TypeError) as err:
            Square("1")

    def test_square_init_with_invalid_size_arg(self):
        """test the initialization of Square instances with invalid
        non integer argument
        """
        with self.assertRaises(TypeError) as err:
            Square(1, "2")

    def test_square_init_with_invalid_y_arg(self):
        """test the initialization of Square instances with invalid
        non integer arguments
        """
        with self.assertRaises(TypeError) as err:
            Square(1, 2, "3")

    def test_square_init_with_neg_size_arg(self):
        """test the initialization of Square instances with invalid
        integers
        """
        with self.assertRaises(ValueError) as err:
            Square(-1)

    def test_square_init_with_neg_x_arg(self):
        """test the initialization of Square instances with invalid
        integers
        """
        with self.assertRaises(ValueError) as err:
            Square(1, -2)

    def test_square_init_with_neg_y_arg(self):
        """test the initialization of Square instances with invalid
        integers
        """
        with self.assertRaises(ValueError) as err:
            Square(1, 2, -3)

    def test_zero_negative_param_init(self):
        """test the initialization of Square instances using invalid
        integers as arguments
        """
        with self.assertRaises(ValueError) as err:
            Square(0)

    def test_none_integer_size_param(self):
        """test the initialization of Square instances using invalid
        non integer arguments
        """
        with self.assertRaises(TypeError) as err:
            Square("size")

        with self.assertRaises(TypeError) as err:
            Square(True)

        with self.assertRaises(TypeError) as err:
            Square(10.5)

    def test_no_param_initialization(self):
        """test the initialization of Square instances using no arguments
        """
        with self.assertRaises(TypeError) as err:
            Square()

    def test_square_area(self):
        """tests the area method of the Square instances"""
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)

    def test_square_size(self):
        """tests the size getter and setter of the Square instances"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 15
        self.assertEqual(s1.size, 15)

        with self.assertRaises(TypeError) as err:
            s1.size = "20"

        with self.assertRaises(ValueError) as err:
            s1.size = -5
