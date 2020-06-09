#!/usr/bin/python3
"""
tests for class rectangle
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """ class 1"""

    def test(self):
        rect = Rectangle(5, 2)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 2)
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.area, 10)

        """ testing on width"""
        self.assertRaises(TypeError, Rectangle, 1.25, 2)
        self.assertRaises(TypeError, Rectangle, "1.25", 2)
        self.assertRaises(ValueError, Rectangle, -3, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        """ testing on height"""
        self.assertRaises(TypeError, Rectangle, 2, 5.25)
        self.assertRaises(TypeError, Rectangle, 2, "5.25")
        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertRaises(ValueError, Rectangle, 2, -3)
        self.assertRaises(TypeError, Rectangle, 1, 2, 1.25, 3)
        self.assertRaises(ValueError, Rectangle, 2, 3, -5, 3)
        self.assertRaises(TypeError, Rectangle, 2, 2, 1, 1.25)
        self.assertRaises(ValueError, Rectangle, 2, 5, 1, -5)

    if __name__ == '__main__':
        unittest.main()
