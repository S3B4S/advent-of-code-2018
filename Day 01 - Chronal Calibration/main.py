from functools import reduce
import fileinput

def transform_data(filename):
    values = []
    for line in fileinput.input(filename):
        values.append(int(line.strip()))
    return values


def part_1():
    values = transform_data('puzzle-input-part1.txt')
    return reduce((lambda x, y: x + y), values)


def part_2():
    values = transform_data('puzzle-input-part2.txt')
    frequency = 0
    seen = set([frequency])
    while True:
        for number in values:
            frequency = frequency + number
            if (frequency in seen):
                return frequency
            seen.add(frequency)


print(part_1()) # 505
print(part_2()) # 72330