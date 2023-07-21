#!/usr/bin/python3
"""This module contains the Test_Rectangle unittest class"""
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """unittest for the models/rectangle module"""

    def test_pep8_square(self):
        """pep8 validation"""
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_rectangle_subclass(self):
        """Tests if Rectangle is a subclass of Base class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rect_init(self):
        """Tests the initialization of Rectangle instances
        with valid integer parameters
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 3)

    def test_non_integer_parameters(self):
        """Tests the initialization of the Rectangle instances with
        invalid parameter(s)
        """
        with self.assertRaises(TypeError) as err:
            Rectangle("width", 7)

        with self.assertRaises(TypeError) as err:
            Rectangle(7, "height")

        with self.assertRaises(TypeError) as err:
            Rectangle("width", "height")

        with self.assertRaises(TypeError) as err:
            Rectangle(True, 5)

        with self.assertRaises(TypeError) as err:
            Rectangle(11, False)

        with self.assertRaises(TypeError) as err:
            Rectangle(6.7, 5)

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10.5)

    def test_no_parameter_initialization(self):
        """Tests the initialization of the Rectangle instances with
        no parameter(s)
        """
        with self.assertRaises(TypeError) as err:
            Rectangle()

    def test_zero_or_negative_parameters(self):
        """Tests the initialization of the Rectangle instances with
        negative integer parameter(s)
        """
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 0)

        with self.assertRaises(ValueError) as err:
            Rectangle(4, 0)

        with self.assertRaises(ValueError) as err:
            Rectangle(0, 8)

        with self.assertRaises(ValueError) as err:
            Rectangle(-19, 10)

        with self.assertRaises(ValueError) as err:
            Rectangle(9, -10)

        with self.assertRaises(ValueError) as err:
            Rectangle(-4, -1)

    def test_rect_area(self):
        """Tests the area function of the Rectangle instance"""
        r1 = Rectangle(10, 12)
        self.assertEqual(r1.area(), 120)
        r2 = Rectangle(10, 10, 1, 3)
        self.assertEqual(r2.area(), 100)

    def test_rect_update_by_args(self):
        """Tests the update function of the Rectangle instance
        using a variable argument(*args) as parameter
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_rect_update_by_kwargs(self):
        """Tests the update function of the Rectangle instance
        using a dictionary(**kwargs) as parameter
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(id=89, height=2, width=3, y=4, x=5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 4)
