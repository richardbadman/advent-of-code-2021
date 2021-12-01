#!/usr/bin/env python3

import os

from os.path import join


INPUT_FILE_NAME = "input.txt"


def main():
    directory = os.path.dirname(
        os.path.relpath(__file__)
    )
    input_file = join(directory, INPUT_FILE_NAME)
    data = _get_measurements(input_file)
    """
    For part 2, I needed a way to group things into triplets, and then produce
    it's sum, this is quite easy with comprehensions

    Example input:
        [1,2,3,4,5,6]
    Example output:
        [[1,2,3], [2,3,4], [3,4,5], ...] -> [6, 9, 13 ...]
    """
    grouped_data = [
        sum(data[n:n+3])
        for n in range(len(data) - 2)
    ]

    """
    This creates a pair of elements per list, where the first element is the
    newest element, and the second element is the predecessor, to make the lambda
    work with None, I had to created a small nested list to flatten to make it work

    Example input:
        [1,2,3]
    Example output:
        [(1, None), (2, 1), (3, 2)]
    """
    group_data = lambda x: zip(
        x,
        [y for z in [[None], x] for y in z]
    )
    _calculate(group_data(data), "one")
    _calculate(group_data(grouped_data), "two")


def _get_measurements(file):
    with open(file) as open_file:
        return [int(line.strip()) for line in open_file]


def _calculate(data, part):
    bigger = lambda x: False if x[1] is None else x[0] > x[1]
    print("Part {part}:\n\t{result}".format(
        part=part,
        result=sum([bigger(data_point) for data_point in data])
    ))


if __name__ == "__main__":
    main()
