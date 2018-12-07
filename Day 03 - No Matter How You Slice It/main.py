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


def find_biggest_values(data):
    maxHeight = 0
    maxWidth = 0

    for row in data:
        currenHeight = row[1] + row[3] - 1
        currentWidth = row[0] + row[2] - 1

        if currenHeight > maxHeight:
            maxHeight = currenHeight

        if currentWidth > maxWidth:
            maxWidth = currentWidth

    return (maxHeight, maxWidth)

# Part 1 entry
def amount_overclaimed_squares(list):
    return 0


class Canvas:
    def __init__(self, data):
        (maxHeight, maxWidth) = find_biggest_values(data)
        self.canvas = [[0 for j in range(0, maxWidth)] for i in range(0, maxHeight)]
    
    def incrementPoint(self, x, y):
        self.canvas[y][x] += 1

    def getValueAtPoint(self, x, y):
        return self.canvas[y][x]

    def print(self):
        for row in self.canvas:
            print(row)


class Test_Part_1(unittest.TestCase):
    def test_transform_data(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        expected = [
            [1, 3, 4, 4],
            [3, 1, 4, 4],
            [5, 5, 2, 2],
        ]
        self.assertEqual(transform_data(values), expected)

    def test_get_max_values(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        self.assertEqual(find_biggest_values(data), (6, 6))

    def test_canvas_1(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        canvas = Canvas(data)
        canvas.incrementPoint(2, 5)
        self.assertEqual(canvas.getValueAtPoint(2, 5), 1)

    def test_canvas_2(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        canvas = Canvas(data)
        canvas.incrementPoint(2, 5)
        canvas.incrementPoint(2, 5)
        self.assertEqual(canvas.getValueAtPoint(2, 5), 2)
    
    def test_simple(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        self.assertEqual(amount_overclaimed_squares(data), 4)