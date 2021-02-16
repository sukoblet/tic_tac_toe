from backend.logic.Board import Board
from backend.logic.Player import Player
from backend.utils.GameState import GameState


class GameStatus:
    def __init__(self):
        self._board = Board()
        # self._player = Player()  # FIXME delete this and perenesty to init
        self._round_is_going = False
        self._game_state = GameState.INITIAL

    def is_game_finished(self):
        if self._board.has_three_in_row() or self._board.is_draw():
            return True
        return False

    def get_winner(self):
        return self._board.get_winner()

    def start_game(self):
        # self._player.score = 0
        self._round_is_going = True
        self._game_state = GameState.START

    def play_game(self):
        self._game_state = GameState.GAME

    def start_round(self):
        self._round_is_going = True

    def finish_round(self, winner):
        self._round_is_going = False
       # self._player.__init__(winner).get_score()

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
