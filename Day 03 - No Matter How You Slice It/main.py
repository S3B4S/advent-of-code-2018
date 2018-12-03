import fileinput
import unittest
import re


def file_to_list(filename):
    values = []
    for line in fileinput.input(filename):
        values.append(line.strip())
    return values


def transform_data(data):
    regex = r"#.*@ (\d),(\d): (\d)x(\d)"
    tuples = [list(re.match(regex, entry).groups()) for entry in data]
    return [[int(digit) for digit in entry] for entry in tuples]


# Part 1 entry
def amount_overclaimed_squares(list):
    return 0


class Canvas:
    def __init__(self):
        self.canvas = [[0 for j in range(0, 1001)] for i in range(0, 1001)]
    
    def incrementPoint(self, x, y):
        self.canvas[x][y] += 1

    def getValueAtPoint(self, x, y):
        return self.canvas[x][y]


class Test_Part_1(unittest.TestCase):
    def test_transform_data(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        expected = [
            [1, 3, 4, 4],
            [3, 1, 4, 4],
            [5, 5, 2, 2],
        ]
        self.assertEqual(transform_data(values), expected)

    def test_canvas_1(self):
        canvas = Canvas()
        canvas.incrementPoint(2, 5)
        self.assertEqual(canvas.getValueAtPoint(2, 5), 1)

    def test_canvas_2(self):
        canvas2 = Canvas()
        canvas2.incrementPoint(2, 5)
        canvas2.incrementPoint(2, 5)
        self.assertEqual(canvas2.getValueAtPoint(2, 5), 2)
    
    def test_simple(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        self.assertEqual(amount_overclaimed_squares(data), 4)