from backend.logic.Board import Board
from backend.utils.GameState import GameState


class GameStatus:
    def __init__(self):
        self._game_state = GameState.INITIAL
        self._winner = None

    def start_game(self):
        self._game_state = GameState.START

    def play_game(self):
        self._game_state = GameState.GAME

    def end_game(self):
        self._game_state = GameState.END

    def is_initial(self):
        return self._game_state == GameState.INITIAL

    def is_start(self):
        return self._game_state == GameState.START

    def is_game(self):
        return self._game_state == GameState.GAME

    def is_end(self):
        return self._game_state == GameState.END

    def set_winner(self, winner):
        self._winner = winner

    def get_winner(self):
        return self._winner
