#!/usr/bin/env python3

import os

from functools import reduce
from os.path import join

NUMBERS = "numbers.txt"
BOARDS = "boards.txt"


class Board:
    numbers_called = 0
    last_called_number = 0
    numbers = []

    winning_combo = None

    def __init__(self, raw_data):
        self.numbers = [Number(value) for value in raw_data]

    def __repr__(self):
        return 'Rows: {rows}\nColumns: {columns}'.format(
            rows=self.rows,
            columns=self.columns
        )

    def process(self, value):
        if self.winning_combo is not None:
            return
        for number in self.numbers:
            number.process(value)

        self.numbers_called += 1
        self.last_called_number = value
        self._check_for_winning_combo()

    def _check_for_winning_combo(self):
        # rows
        for i in range(0,24,5):
            if all([number.marked for number in self.numbers[i:i+5]]):
                self.winning_combo = self.numbers[i:i+5]
                return
        # columns
        for i in range(0,5):
            if all([number.marked for number in self.numbers[i::5]]):
                self.winning_combo = self.numbers[i::5]
                return

    def calculate(self):
        unmarked_values = [
            number
            for number in self.numbers
            if number.marked == False
        ]
        total = sum(unmarked_values)
        print("Sum of other values: {total}, Last winning number: {last_number}\n\tProduct: {result}".format(
            total=total,
            last_number=self.last_called_number,
            result=total*self.last_called_number
        ))



class Number:
    value = 0
    marked = False

    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return '{}'.format(self.value)

    def __radd__(self, value):
        return self.value + value

    def process(self, value):
        if self.value != value:
            return
        self.marked = True


def _generate_rows(data):
    rows = [line.split() for line in data[:-1]]
    return [[Number(y) for y in x] for x in rows]


def _generate_columns(data):
    # Convert to list of lists and remove blank ''
    data_formatted = [line.split() for line in data[:-1]]
    # Transform the matrix
    transformed = [list(line) for line in ([*zip(*data_formatted)])]
    return [[Number(y) for y in x] for x in transformed]


def main():
    directory = os.path.dirname(os.path.relpath(__file__))
    numbers_file = join(directory, NUMBERS)
    boards_file = join(directory, BOARDS)

    numbers = _get_numbers(numbers_file)
    boards = _get_boards(boards_file)

    for number in numbers:
        for board in boards:
            board.process(number)

    sorted_boards = sorted(boards, key=lambda x: x.numbers_called)
    winning_board = sorted_boards[0]
    loosing_board = sorted_boards[-1]
    print("Number of turns: {count}, Winning row/column: {win}".format(
        count=winning_board.numbers_called,
        win=winning_board.winning_row or winning_board.winning_column
    ))
    winning_board.calculate()
    print("Number of turns: {count}, Winning row/column: {win}".format(
        count=loosing_board.numbers_called,
        win=loosing_board.winning_row or loosing_board.winning_column
    ))
    loosing_board.calculate()


def _get_numbers(file):
    with open(file) as open_file:
        return [int(number) for number in open_file.read().split(',')]

def _get_boards(file):
    def _get_data(file):
        with open(file) as open_file:
            return [line.strip() for line in open_file]
    data = _get_data(file)
    boards = []

    while len(data) > 0:
        raw_data = reduce(lambda x,y: x+y, [x.split() for x in data[:6]])
        boards.append(Board(raw_data))
        del data[:6]
    return boards



if __name__ == "__main__":
    main()
