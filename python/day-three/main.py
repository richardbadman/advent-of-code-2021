#!/usr/bin/env python3

import os

from os.path import join


INPUT_FILE_NAME = "input.txt"


def main():
    directory = os.path.dirname(os.path.relpath(__file__))
    input_file = join(directory, INPUT_FILE_NAME)

    _part_one(_get_data(input_file))
    _part_two(_get_data(input_file))


def _part_one(data):
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


def _part_two(data):
    oxygen = data.copy()
    most_common = lambda x: '0' if x.count('0') > x.count('1') else '1'

    carbon = data.copy()
    least_common = lambda x: '1' if x.count('1') < x.count('0') else '0'

    oxygen_result = ''.join(_get_result(oxygen, most_common)[0])
    carbon_result = ''.join(_get_result(carbon, least_common)[0])

    print("Oxygen: {oxygen}\nCarbon: {carbon}\n\tResult: {result}".format(
        oxygen=oxygen_result,
        carbon=carbon_result,
        result=(int(oxygen_result, 2) * int(carbon_result, 2))
    ))


def _get_result(data, function):
    n = 0
    while True:
        try:
            if len(data) == 1:
                break
            vertical = [bits[n] for bits in data]
            variable = function(vertical)
            data = [
                bits for bits in data
                if bits[n] == variable
            ]
            n += 1
        except IndexError:
            break
    return data


def _get_data(file):
    with open(file) as open_file:
        return [[bit for bit in line.strip()] for line in open_file]


if __name__ == "__main__":
    main()
