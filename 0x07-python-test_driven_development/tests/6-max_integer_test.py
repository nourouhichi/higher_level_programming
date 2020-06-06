#!/usr/bin/python3
"""
max_integer unittest
"""


max_integer = __import__('6-max_integer').max_integer
import unittest

class TestMaxInteger(unittest.TestCase):
    """unittest class"""


    def test_max_integer(self):
        """ function 1"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-58, 2, 2]), 2)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-1, 50, 5]), 50)
