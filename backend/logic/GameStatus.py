from backend.logic.Board import Board
from backend.logic.Player import Player
from backend.utils.GameState import GameState


class GameStatus:
    def __init__(self):
        self._board = Board()
        # self._player = Player()  # FIXME delete this and perenesty to init
        self._round_is_going = False
        self._game_state = GameState.INITIAL

    def start_round(self):
        self._round_is_going = True

    def get_winner(self):
        return self._board.get_winner()

    def finish_round(self, winner):
        self._round_is_going = False

    def is_round_active(self):
        return self._round_is_going

    def play_game(self):
        self._game_state = GameState.GAME

    def start_game(self):
        # self._player.score = 0
        self.start_round()
        self._game_state = GameState.START

    def end_game(self):
        # self._player.score = 0
        self._game_state = GameState.END

    def is_initial(self):
        return self._game_state == GameState.INITIAL

    def is_start(self):
        return self._game_state == GameState.START

    def is_game(self):
        return self._game_state == GameState.GAME

    def is_end(self):
        return self._game_state == GameState.END

    def is_game_finished(self):
        if self._board.has_three_in_row() or self._board.is_draw():
            return True
        return False



