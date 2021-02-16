import pygame
import os


class Drawer:
    def __init__(self, surface):
        self._surface = surface

        self._SIGN_COLOR = (232, 232, 232)
        self._NOUGHT_WIDTH = 10
        self._CROSS_WIDTH = 15

        self._FONT_PATH = os.path.join('fonts', 'arial.ttf')

    def draw_cross(self, center, side):
        x, y = center
        half_side = side // 2

        pygame.draw.line(self._surface, self._SIGN_COLOR,
                         (x - half_side, y - half_side), (x + half_side, y + half_side), self._CROSS_WIDTH)
        pygame.draw.line(self._surface, self._SIGN_COLOR,
                         (x - half_side, y + half_side), (x + half_side, y - half_side), self._CROSS_WIDTH)

        pygame.display.update()

    def draw_nought(self, center, side):
        pygame.draw.circle(self._surface, self._SIGN_COLOR, center, side // 2, self._NOUGHT_WIDTH)

        pygame.display.update()

    def draw_text(self, text, font_size, center, font_color=(232, 232, 232)):
        font = pygame.font.Font(self._FONT_PATH, font_size)
        text_surface = font.render(text, True, font_color)

        width, height = text_surface.get_size()

        x, y = center

        self._surface.blit(text_surface, (x - width // 2, y - height // 2))

        pygame.display.update()

    def draw_button(self):
        pass
