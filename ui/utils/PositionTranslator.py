class PositionTranslator:
    def __init__(self, x_offset, y_offset, cell_side, line_width):
        self._x_offset = x_offset
        self._y_offset = y_offset
        self._cell_side = cell_side
        self._line_width = line_width

        self._x_min = self._x_offset + self._line_width
        self._y_min = self._y_offset + self._line_width
        self._x_max = self._x_offset + 4 * self._line_width + 3 * self._cell_side
        self._y_max = self._y_offset + 4 * self._line_width + 3 * self._cell_side

    def to_row_column(self, x, y):
        if x <= self._x_min or x >= self._x_max or y <= self._y_min or y >= self._y_max:
            return None

        x = x - self._line_width - self._x_offset
        y = y - self._line_width - self._y_offset

        localx = x % (self._cell_side + self._line_width)
        localy = y % (self._cell_side + self._line_width)

        if localx > self._cell_side or localy > self._cell_side:
            return None

        return y // (self._cell_side + self._line_width),  x // (self._cell_side + self._line_width)

    def to_xy(self, row, col):
        return self._y_min + col * (self._cell_side + self._line_width) + self._cell_side // 2, \
               self._x_min + row * (self._cell_side + self._line_width) + self._cell_side // 2
