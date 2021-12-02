#!/usr/bin/env python3

import os

from os.path import join


INPUT_FILE_NAME = "input.txt"


def main():
    directory = os.path.dirname(os.path.relpath(__file__))
    input_file = join(directory, INPUT_FILE_NAME)

    horizontal = 0
    depth = 0
    data = _get_data(input_file)

    for instruction in data:
        if instruction[0] == "forward":
            horizontal += int(instruction[1])
        if instruction[0] == "up":
            depth -= int(instruction[1])
        if instruction[0] == "down":
            depth += int(instruction[1])
    print("End 'co-ords': Horizontal: {horizontal}, Depth: {depth}\n\t{product}".format(
        horizontal=horizontal,
        depth=depth,
        product=(horizontal * depth)
    ))


def _get_data(file):
    with open(file) as open_file:
        return [line.split() for line in open_file]


if __name__ == "__main__":
    main()
