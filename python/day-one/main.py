#!/usr/bin/env python3

import os

from os.path import join


INPUT_FILE_NAME = "input.txt"


def main():
    directory = os.path.dirname(
        os.path.relpath(__file__)
    )
    input_file = join(directory, INPUT_FILE_NAME)
    _measurements = _get_measurements(input_file)
    measurements = zip(
        _measurements,
        [x for y in [[None], _measurements] for x in y]
    )
    bigger = lambda x: False if x[1] is None else x[0] > x[1]
    print(sum(
        [bigger(measurement) for measurement in measurements]
    ))


def _get_measurements(file):
    with open(file) as open_file:
        return [int(line.strip()) for line in open_file]


if __name__ == "__main__":
    main()
