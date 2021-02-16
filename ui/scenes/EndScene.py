import sys
import pygame

from backend.utils.Sign import Sign
from ui.utils.Drawer import Drawer


class EndScene:
    def __init__(self, game, window):
        self._status = game.get_status()
        self._window = window
        self._window.fill((51, 51, 51))
        self._drawer = Drawer(pygame.display.get_surface())

    def render(self):
        winner = self._status.get_winner()

        height = self._window.get_height()

        if winner != Sign.NO_SIGN:
            text_args = ['Winner', int(0.2 * height), (self._window.get_width() // 2, int(0.2 * height))]
            self._drawer.draw_text(*text_args)

            draw_args = [(self._window.get_width() // 2, int(0.6 * height)), int(0.4 * height)]
            if winner == Sign.CROSS:
                self._drawer.draw_cross(*draw_args)
            if winner == Sign.NOUGHT:
                self._drawer.draw_nought(*draw_args)
        else:
            text_args = ['Draw', int(0.3 * height), (self._window.get_width() // 2, height // 2)]
            self._drawer.draw_text(*text_args)

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
