from backend.utils.Sign import Sign


class Board:
    def __init__(self):
        self._board = [[-1 for _ in range(3)] for _ in range(3)]

    def has_three_in_row(self):
        return self.get_winner() is not None

    def get_winner(self):
        for row in range(0, 3):
            if self._board[row][0] == self._board[row][1] == self._board[row][2] \
                    and Sign(self._board[row][0]) != Sign.NO_SIGN:
                return Sign(self._board[row][0])
            if self._board[0][row] == self._board[1][row] == self._board[2][row] \
                    and Sign(self._board[0][row]) != Sign.NO_SIGN:
                return Sign(self._board[0][row])

        if self._board[0][0] == self._board[1][1] == self._board[2][2] \
                and Sign(self._board[0][0]) != Sign.NO_SIGN:
            return Sign(self._board[0][0])
        elif self._board[0][2] == self._board[1][1] == self._board[2][0] \
                and Sign(self._board[0][2]) != Sign.NO_SIGN:
            return Sign(self._board[0][2])

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
        self._board[row][col] = Sign.CROSS.value
        self.print_board()

    def add_nought(self, row, col):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        self._board[row][col] = Sign.NOUGHT.value
        self.print_board()

    def is_taken(self, row, col):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        if self._board[row][col] == Sign.NO_SIGN.value:
            return False
        else:
            return True

    def print_board(self):
        print(*self._board[0])
        print(*self._board[1])
        print(*self._board[2])