import fileinput


def transform_data(filename):
    values = []
    for line in fileinput.input(filename):
        values.append(line.strip())
    return values


def part_1():
    values = transform_data('puzzle-input.txt')


print(part_1())