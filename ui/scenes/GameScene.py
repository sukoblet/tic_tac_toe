import pygame

from ui.EventsListener import EventsListener
from ui.scenes.elements.BoardView import BoardView


class GameScene:
    def __init__(self, game, window, translator, fps, board_view):
        self._game = game
        self._window = window
        self._status = game.get_status()
        self._board_view = board_view
        self._listener = EventsListener(self._status, self._game.get_events_handler(), fps, translator)

    def render(self):
        self._board_view.render()

    # TODO calls draw_cross, drow_nought, and so on, the question is from where it takes info
    # TODO we can use translator that will be here
    def render_board_state(self):
        pass

    def get_listener(self):
        return self._listener

