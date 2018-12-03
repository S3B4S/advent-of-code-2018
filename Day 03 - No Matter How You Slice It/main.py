import fileinput
import unittest
import re


class Test_Part_1(unittest.TestCase):
    def test_transform_data(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        expected = [
            [1, 3, 4, 4],
            [3, 1, 4, 4],
            [5, 5, 2, 2],
        ]
        result = transform_data(values)
        self.assertEqual(result, expected)