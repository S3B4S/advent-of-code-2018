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


def part_2():
    values = transform_data('puzzle-input.txt')
    return find_similar_ids(values)


print(part_1()) # 8715
print(part_2()) # fvstwblgqkhpuixdrnevmaycd