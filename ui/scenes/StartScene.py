import sys
import pygame

from ui.utils.Drawer import Drawer


class StartScene:
    def __init__(self, game, window):
        self._game = game
        self._window = window
        self._window.fill((51, 51, 51))
        self._status = game.get_status()

        self._BUTTON_COLOR = (198, 198, 198)

        button_width, button_height = (300, 140)
        self._start_button = pygame.Rect((self._window.get_width() // 2 - button_width // 2,
                                          self._window.get_height() // 2 - button_height // 2),
                                         (button_width, button_height))

    def render(self):
        drawer = Drawer(pygame.display.get_surface())
        center = (self._window.get_width() // 2, self._window.get_height() // 2)

        pygame.draw.rect(self._window, self._BUTTON_COLOR, self._start_button)
        drawer.draw_text('Start', 100, center, font_color=(51, 51, 51))

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if self._start_button.collidepoint(event.pos):
                self._status.play_game()
