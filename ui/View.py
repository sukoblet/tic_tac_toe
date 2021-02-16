from ui.scenes.StartScene import StartScene
from ui.scenes.GameScene import GameScene
from ui.scenes.EndScene import EndScene

from ui.EventsListener import EventsListener

import pygame

from ui.scenes.elements.BoardView import BoardView
from ui.utils.PositionTranslator import PositionTranslator


class View:
    def __init__(self, game, fps):
        self._fps = fps

        self._game = game
        self._status = game.get_status()

        pygame.init()
        self._initialize_sizes()
        self._window = pygame.display.set_mode((self._window_width, self._window_height))
        pygame.display.set_caption('Tic Tac Toe by Sukoblet')
        self._window.fill((51, 51, 51))
        pygame.display.update()

        self._start_scene = None
        self._game_scene = None
        self._end_scene = None

    def _initialize_sizes(self):
        self._cell_side = 150
        self._line_width = 16
        self._padding = 30

        self._spacing = self._padding

        self._status_height = 100
        self._window_height = 2 * self._padding + self._status_height + 4 * self._line_width \
                              + 3 * self._cell_side + self._spacing

        self._window_width = 2 * self._padding + 4 * self._line_width + 3 * self._cell_side
        self._status_width = self._window_width - 2 * self._padding

    def start(self):
        self._start_scene = StartScene(self._game, self._window)

        return self._start_scene

    def play(self):
        board_side = 4 * self._line_width + 3 * self._cell_side
        x_offset = self._padding
        y_offset = self._padding + self._status_height + self._spacing
        board_view = BoardView((board_side, board_side), self._cell_side, self._line_width, (x_offset, y_offset))
        translator = PositionTranslator(x_offset, y_offset, self._cell_side, self._line_width)
        self._game_scene = GameScene(self._game, self._window, translator, self._fps, board_view)

        return self._game_scene

    def end(self):  # TODO show end scene
        pass

    # TODO here may be methods for showing the game scene and end scene, as well as rounds switching
