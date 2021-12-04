#!/usr/bin/env python3

import os

from os.path import join

NUMBERS = "numbers.txt"
BOARDS = "boards.txt"


class Board:
    numbers_called = 0
    last_called_number = 0
    rows = []
    columns = []

    winning_row = None
    winning_column = None

    def __init__(self, raw_data):
        self.rows = _generate_rows(raw_data.copy())
        self.columns = _generate_columns(raw_data.copy())

    def __repr__(self):
        return 'Rows: {rows}\nColumns: {columns}'.format(
            rows=self.rows,
            columns=self.columns
        )

    def process(self, value):
        if self.winning_row is not None or self.winning_column is not None:
            return
        self._process_row(value)
        self._process_column(value)
        self.numbers_called += 1
        self.last_called_number = value

    def _process_row(self, value):
        for row in self.rows:
            for number in row:
                number.process(value)
            if all([number.marked for number in row]):
                winning_row = row
                break
            else:
                continue
            break

    def _process_column(self, value):
        for column in self.columns:
            for number in column:
                number.process(value)
            if all([number.marked for number in column]):
                self.winning_column = column
                break
            else:
                continue
            break

    def calculate(self):
        unmarked_values = []
        if self.winning_row:
            unmarked_values = [
                number
                for row in self.rows
                if row != self.winning_row
                for number in row
                if number.marked == False
            ]
        else:
            unmarked_values = [
                number
                for column in self.columns
                if column != self.winning_column
                for number in column
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

    winning_board = sorted(boards, key=lambda x: x.numbers_called)[0]
    print("Number of turns: {count}, Winning row/column: {win}".format(
        count=winning_board.numbers_called,
        win=winning_board.winning_row or winning_board.winning_column
    ))
    winning_board.calculate()


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
        subset = data[:6]
        boards.append(Board(subset))
        del data[:6]
    return boards



if __name__ == "__main__":
    main()
