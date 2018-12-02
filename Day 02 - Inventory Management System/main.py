from functools import reduce
import fileinput
import unittest


def transform_data(filename):
    values = []
    for line in fileinput.input(filename):
        values.append(line.strip())
    return values


def count_valid_boxes(acc, curr):
    twos = 0
    threes = 0

    for char in curr:
        count = curr.count(char)
        if (twos == 0 and count == 2):
            twos = 1
        if (threes == 0 and count == 3):
            threes = 1
        if (twos == 1 and threes == 1):
            break

    return (acc[0] + twos, acc[1] + threes)


def part_1(values):
    count = reduce(count_valid_boxes, values, (0, 0))
    return count[0] * count[1]


def differ_by_one_char(id, other_id):
    count_different_chars = 0
    index_different_char = -1

    for index, char in enumerate(id):
        if (other_id[index] != char):
            count_different_chars += 1
            index_different_char = index

    if (count_different_chars == 1):
        return id[:index_different_char] + id[index_different_char + 1:]


def find_similar_ids(id_list):
    for index, id in enumerate(id_list):
        for other_id in id_list[index:]:
            value = differ_by_one_char(id, other_id)
            if (value is not None):
                return value
            else:
                continue


def part_2(values):
    return find_similar_ids(values)


class Test_Part_1(unittest.TestCase):
    def test_simple(self):
        values = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
        self.assertEqual(part_1(values), 12)
    
    def test_puzzle_input(self):
        values = transform_data('puzzle-input.txt')
        self.assertEqual(part_1(values), 8715)


class Test_Part_2(unittest.TestCase):
    def test_simple(self):
        values = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
        self.assertEqual(part_2(values), 'fgij')

    def test_puzzle_input(self):
        values = transform_data('puzzle-input.txt')
        self.assertEqual(part_2(values), 'fvstwblgqkhpuixdrnevmaycd')