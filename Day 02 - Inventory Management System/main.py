from functools import reduce
import fileinput


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


def part_1():
    values = transform_data('puzzle-input.txt')
    count = reduce(count_valid_boxes, values, (0, 0))
    return count[0] * count[1]


print(part_1()) # 8715