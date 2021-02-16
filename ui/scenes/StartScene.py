import sys
import pygame


class StartScene:
    def __init__(self, game, window):
        self._game = game
        self._window = window
        self._status = game.get_status()

        # TODO change magic numbers
        self._start_button = pygame.Rect((self._window.get_width() // 2 - 75, self._window.get_height() // 2 - 35),
                                         (150, 70))

        # TODO maybe draw using Drawer object

    def render(self):
        pygame.draw.rect(self._window, (198, 198, 198), self._start_button)
        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if self._start_button.collidepoint(event.pos):
                self._status.play_game()
