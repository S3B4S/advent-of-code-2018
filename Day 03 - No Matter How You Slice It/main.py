import fileinput
import unittest
import re


def file_to_list(filename):
    values = []
    for line in fileinput.input(filename):
        values.append(line.strip())
    return values


def get_digits(list):
    return [int(entry) for entry in list if entry.isdigit()]


def transform_data(list):
    split = [re.split(' |x|,|:', entry) for entry in list]
    return [get_digits(entry) for entry in split]


# Part 1 function entry
def amount_overclaimed_squares(list):
    return 0

class Test_Part_1(unittest.TestCase):
    def test_transform_data(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        expected = [
            [1, 3, 4, 4],
            [3, 1, 4, 4],
            [5, 5, 2, 2],
        ]
        self.assertEqual(transform_data(values), expected)

    def test_simple(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        self.assertEqual(amount_overclaimed_squares(data), 4)