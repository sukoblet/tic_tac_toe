import pygame

from backend.utils.Sign import Sign
from ui.utils.Drawer import Drawer


class BoardView:
    def __init__(self, size, cs, lw, offset, board, translator):
        self._line_width = lw
        self._cell_side = cs
        self._LINE_COLOR = (80, 80, 80)
        self._RECT_COLOR = (140, 140, 140)
        self._x_off, self._y_off = offset
        self._width, self._height = size

        self._board = board
        self._translator = translator

        self._drawer = Drawer(pygame.display.get_surface())

        assert self._line_width % 2 == 0, 'Line width value must be even to draw lines in a pretty way'
        assert self._cell_side % 2 == 0, 'Cell side value must be even to draw cells in a pretty way'

    def render(self):
        surf = pygame.display.get_surface()

        y_start = self._y_off + 1
        y_end = self._y_off + self._height
        for x in range(self._x_off + self._line_width // 2, self._x_off + self._width,
                       self._line_width + self._cell_side):
            pygame.draw.line(surf, self._LINE_COLOR, (x, y_start), (x, y_end), self._line_width)

        x_start = self._x_off + 1
        x_end = self._x_off + self._width
        for y in range(self._y_off + self._line_width // 2, self._y_off + self._height,
                       self._line_width + self._cell_side):
            pygame.draw.line(surf, self._LINE_COLOR, (x_start, y), (x_end, y), self._line_width)

        for col, x in enumerate(
                range(self._x_off + self._line_width + 1, self._width, self._line_width + self._cell_side)):
            for row, y in enumerate(
                    range(self._y_off + self._line_width + 1, self._height, self._line_width + self._cell_side)):
                rect = pygame.Rect((x, y), (self._cell_side, self._cell_side))
                pygame.draw.rect(surf, self._RECT_COLOR, rect)

        pygame.display.update()

    def update(self, row, col):
        sign = self._board.get_sign(row, col)
        if sign == Sign.CROSS:
            self._drawer.draw_cross(self._translator.to_xy(row, col), int(0.8 * self._cell_side))
        if sign == Sign.NOUGHT:
            self._drawer.draw_nought(self._translator.to_xy(row, col), int(0.8 * self._cell_side))
