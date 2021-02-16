from backend.logic.Board import Board
from backend.logic.EventsHandler import EventsHandler
from backend.logic.GameStatus import GameStatus
from backend.utils.Sign import Sign


class Game:
    def __init__(self):
        self._board = Board()
        self._status = GameStatus()
        self._handler = EventsHandler(self)

        self._queue = [Sign.CROSS, Sign.NOUGHT]
        self._current = 0

    def make_move(self, row, col):
        if not self._board.is_taken(row, col):
            self._board.add_sign(row, col, self._queue[self._current])
            self._current = 1 - self._current

            winner = self._board.get_winner()
            if winner is not None:
                self._status.set_winner(winner)
                self._status.end_game()

    def get_status(self):
        return self._status

    def get_events_handler(self):
        return self._handler

    def get_board(self):
        return self._board
