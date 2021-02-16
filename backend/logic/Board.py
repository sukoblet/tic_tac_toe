from backend.utils.Sign import Sign


class Board:
    def __init__(self):
        self._board = [[-1 for _ in range(3)] for _ in range(3)]

    def has_three_in_row(self):
        winner = self.get_winner()
        return winner is not None and winner != Sign.NO_SIGN

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

        return Sign.NO_SIGN if self._is_everything_taken() else None

    def _is_everything_taken(self):
        for row in range(0, 3):
            for col in range(0, 3):
                if not self.is_taken(row, col):
                    return False
        return True

    def is_draw(self):
        return self._is_everything_taken() and not self.has_three_in_row()

    def add_sign(self, row, col, sign):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        if not isinstance(sign, Sign) or sign == Sign.NO_SIGN:
            raise ValueError('Argument sign must be the instance of Sign class and have a value of CROSS or NOUGHT')
        self._board[row][col] = sign.value

    def is_taken(self, row, col):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        return not Sign(self._board[row][col]) == Sign.NO_SIGN

    def get_sign(self, row, col):
        if not 0 <= row < 3 or not 0 <= col < 3:
            raise ValueError('Row and column must be the not negative integers that are less than 3 ')
        return Sign(self._board[row][col])
