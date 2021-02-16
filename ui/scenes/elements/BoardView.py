import pygame


class BoardView:
    def __init__(self, size, cs, lw, offset):
        self._line_width = lw
        self._cell_side = cs
        self._LINE_COLOR = (80, 80, 80)
        self._RECT_COLOR = (140, 140, 140)
        self._x_off, self._y_off = offset
        self._width, self._height = size

        assert self._line_width % 2 == 0, 'Line width value must be even to draw lines in a pretty way'
        assert self._cell_side % 2 == 0, 'Cell side value must be even to draw cells in a pretty way'

    def render(self):
        # TODO maybe use drawer for this
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

    def draw_cross(self, row, column):
        pass

    def draw_nought(self, row, column):
        pass

    def draw_winner(self, row1, column1, row2, column2):
        pass
