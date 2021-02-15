import sys


class Board:
    def __init__(self):
        self._board = [[-1 for _ in range(3)] for _ in range(3)]
        self._NOUGHT = 0
        self._CROSS = 1

    def has_three_in_row(self):
        return self.get_winner() is not None

    def get_winner(self):
        for row in range(0, 3):
            for col in range(0, 3):
                if self._board[row][col] == self._board[row][col] == self._board[row][col] == self._NOUGHT:
                    return 'o'
                elif self._board[row][col] == self._board[row][col] == self._board[row][col] == self._CROSS:
                    return 'x'
        if self._board[0][0] == self._board[1][1] == self._board[2][2] or self._board[0][2] == self._board[1][1] == \
                self._board[2][0] == self._NOUGHT:
            return 'o'
        elif self._board[0][0] == self._board[1][1] == self._board[2][2] or self._board[0][2] == self._board[1][1] == \
                self._board[2][0] == self._CROSS:
            return 'x'

        return None

    def is_draw(self):
        for row in range(0, 3):
            for col in range(0, 3):
                if not self.is_taken(row, col):
                    return False
        if self.has_three_in_row():
            return False
        return True

    def add_cross(self, row, col):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        self._board[row][col] = self._CROSS

    def add_nought(self, row, col):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        self._board[row][col] = self._NOUGHT

    def is_taken(self, row, col):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        if self._board[row][col] == -1:
            return False
        else:
            return True
