class EventsHandler:
    def __init__(self, game):
        self._game = game

    def callback_onclick(self, row, col):
        self._game.make_move(row, col)
