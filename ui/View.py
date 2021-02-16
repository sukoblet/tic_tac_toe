from ui.scenes.StartScene import StartScene
from ui.scenes.GameScene import GameScene
from ui.scenes.EndScene import EndScene

from ui.EventsListener import EventsListener

import pygame


class View:
    def __init__(self, game, fps):
        self._fps = fps

        self._game = game
        self._status = game.get_status()  # TODO needs to be added
        # TODO get_events_handler() needs to be implemented
        self._listener = EventsListener(self._status, game.get_events_handler(), self._fps)

        pygame.init()
        self._initialize_sizes()
        self._window = pygame.display.set_mode((self._window_width, self._window_height))
        pygame.display.set_caption('Tic Tac Toe by Sukoblet')
        self._window.fill((51, 51, 51))
        pygame.display.update()

        # TODO add translator object
        self._listener.set_translator(None)  # TODO set translator (replace None with the object)

        self._start_scene = None
        self._game_scene = None
        self._end_scene = None

    def _initialize_sizes(self):
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

        # TODO maybe differ window size basing on the screen resolution

        self._cell_side = 150
        self._line_width = 15
        self._padding = 30

        self._spacing = self._padding

        self._status_height = 100
        self._window_height = 2 * self._padding + self._status_height + 4 * self._line_width \
                              + 3 * self._cell_side + self._spacing

        self._window_width = 2 * self._padding + 4 * self._line_width + 3 * self._cell_side
        self._status_width = self._window_width - 2 * self._padding

    def start(self):  # TODO this will be rewritten to show only start scene
        self._start_scene = StartScene(self._game, self._window)

        return self._start_scene

    def play(self):  # TODO show game scene
        print('play')

    def end(self):  # TODO show end scene
        pass

    # TODO here may be methods for showing the game scene and end scene, as well as rounds switching
