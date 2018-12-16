import fileinput
import unittest
import re


def file_to_list(filename):
    values = []
    for line in fileinput.input(filename):
        values.append(line.strip())
    return values


def transform_data(data):
    regex = r"#.*@ (\d*),(\d*): (\d*)x(\d*)"
    tuples = [list(re.match(regex, entry).groups()) for entry in data]
    return [[int(digit) for digit in entry] for entry in tuples]


def find_biggest_values(data):
    maxHeight = 0
    maxWidth = 0

    for row in data:
        currenHeight = row[1] + row[3]
        currentWidth = row[0] + row[2]

        if currenHeight > maxHeight:
            maxHeight = currenHeight

        if currentWidth > maxWidth:
            maxWidth = currentWidth

    return (maxHeight, maxWidth)


# Part 1 entry
def amount_overclaimed_squares(data):
    (maxHeight, maxWidth) = find_biggest_values(data)
    canvas = Canvas(maxHeight, maxWidth)
    canvas.mark_canvas(data)

    count = 0
    for row in canvas.canvas:
        for cell in row:
            if cell > 1:
                count += 1
    
    return count


# Part 2 entry
def find_perfect_claim(data):
    (maxHeight, maxWidth) = find_biggest_values(data)
    canvas = Canvas(maxHeight, maxWidth)
    canvas.mark_canvas(data)

    for index, entry in enumerate(data):
        perfect = True
        x = entry[0]
        y = entry[1]
        dx = entry[2]
        dy = entry[3]

        for i in range(x, x + dx):
                for j in range(y, y + dy):
                    if canvas.get_value(i, j) != 1:
                        perfect = False
        
        if perfect:
            return index + 1

    return -1


class Canvas:
    def __init__(self, height, width):
        self.canvas = [[0 for j in range(0, width + 1)] for i in range(0, height + 1)]
    
    def mark_canvas(self, data):
        for entry in data:
            x = entry[0]
            y = entry[1]
            dx = entry[2]
            dy = entry[3]

            for i in range(x, x + dx):
                for j in range(y, y + dy):
                    self.increment_point(i, j)

    def increment_point(self, x, y):
        self.canvas[y][x] += 1

    def get_value(self, x, y):
        return self.canvas[y][x]

    def print(self):
        for row in self.canvas:
            print(row)


class Test_General(unittest.TestCase):
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
        self.assertEqual(find_biggest_values(data), (7, 7))

    def test_canvas_1(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        (maxHeight, maxWidth) = find_biggest_values(data)
        canvas = Canvas(maxHeight, maxWidth)
        canvas.increment_point(2, 5)
        self.assertEqual(canvas.get_value(2, 5), 1)

    def test_canvas_2(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        (maxHeight, maxWidth) = find_biggest_values(data)
        canvas = Canvas(maxHeight, maxWidth)
        canvas.increment_point(2, 5)
        canvas.increment_point(2, 5)
        self.assertEqual(canvas.get_value(2, 5), 2)


class Test_Part_1(unittest.TestCase):    
    def test_simple(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        self.assertEqual(amount_overclaimed_squares(data), 4)

    def test_puzzle_input(self):
        values = file_to_list('puzzle-input.txt')
        data = transform_data(values)
        self.assertEqual(amount_overclaimed_squares(data), 124850)


class Test_Part_2(unittest.TestCase):
    def test_simple(self):
        values = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        data = transform_data(values)
        self.assertEqual(find_perfect_claim(data), 3)

    def test_puzzle_input(self):
        values = file_to_list('puzzle-input.txt')
        data = transform_data(values)
        self.assertEqual(find_perfect_claim(data), 1097)