class PositionTranslator:
    def __init__(self, x_offset, y_offset, cell_side, line_width):
        self._x_offset = x_offset
        self._y_offset = y_offset
        self._cell_side = cell_side
        self._line_width = line_width

    def to_row_column(self, x, y):
        pass

    def to_xy(self, row, column):
        pass
