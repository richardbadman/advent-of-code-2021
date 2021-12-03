#!/usr/bin/env python3

import os

from os.path import join


INPUT_FILE_NAME = "input.txt"


def main():
    directory = os.path.dirname(os.path.relpath(__file__))
    input_file = join(directory, INPUT_FILE_NAME)

    data = _get_data(input_file)
    gamma = ''
    while True:
        try:
            vertical = [bits.pop(0) for bits in data]
            if vertical.count('0') > vertical.count('1'):
                gamma += '0'
            else:
                gamma += '1'
        except IndexError:
            break
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    print("Gamma: {gamma}, Epsilon: {epsilon}\n\t{value}".format(
        gamma=gamma,
        epsilon=epsilon,
        value=(int(gamma, 2) * int(epsilon, 2))
    ))

def _get_data(file):
    with open(file) as open_file:
        return [[bit for bit in line.strip()] for line in open_file]


if __name__ == "__main__":
    main()

