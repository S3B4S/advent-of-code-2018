from functools import reduce
import fileinput
import unittest


def transform_data(filename):
    values = []
    for line in fileinput.input(filename):
        values.append(int(line.strip()))
    return values


def part_1(values):
    return reduce((lambda x, y: x + y), values)


def part_2(values):
    frequency = 0
    seen = set([frequency])
    while True:
        for number in values:
            frequency = frequency + number
            if (frequency in seen):
                return frequency
            seen.add(frequency)


class Test_Part_1(unittest.TestCase):
    def test_simple_1(self):
        values = [1, 1, 1]
        self.assertEqual(part_1(values), 3)

    def test_simple_2(self):
        values = [1, 1, -2]
        self.assertEqual(part_1(values), 0)

    def test_simple_3(self):
        values = [-1, -2, -3]
        self.assertEqual(part_1(values), -6)

    def test_puzzle_input(self):
        values = transform_data('puzzle-input.txt')
        self.assertEqual(part_1(values), 505)


class Test_Part_2(unittest.TestCase):
    def test_simple(self):
        values = [1, -1]
        self.assertEqual(part_2(values), 0)

    def test_with_loop_1(self):
        values = [3, 3, 4, -2, -4]
        self.assertEqual(part_2(values), 10)

    def test_with_loop_2(self):
        values = [-6, 3, 8, 5, -6]
        self.assertEqual(part_2(values), 5)

    def test_with_loop_3(self):
        values = [7, 7, -2, -7, -4]
        self.assertEqual(part_2(values), 14)

    def test_puzzle_input(self):
        values = transform_data('puzzle-input.txt')
        self.assertEqual(part_2(values), 72330)