#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer_test').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_all_same_numbers(self):
        """Test list where all numbers are the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_single_element_list(self):
        """Test list with single element"""
        self.assertEqual(max_integer([8]), 8)

    def test_max_at_beginning(self):
        """Test list with max at beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        """Test list with max at end"""
        self.assertEqual(max_integer([1, 3, 2, 9]), 9)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -22, -38, -52]), -1)

    def test_duplicates(self):
        """Test list with duplicate max values"""
        self.assertEqual(max_integer([2, 4, 4, 1]), 4)


if __name__ == '__main__':
    unittest.main()
