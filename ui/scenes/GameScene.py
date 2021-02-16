from ui.utils.EventsListener import EventsListener


class GameScene:
    def __init__(self, game, window, translator, fps, board_view):
        self._game = game
        self._window = window
        self._window.fill((51, 51, 51))
        self._status = game.get_status()
        self._board_view = board_view
        self._listener = EventsListener(self._status, self._game.get_events_handler(), fps, translator, self)

    def render(self):
        self._board_view.render()

    def render_board_state(self, row, col):
        self._board_view.update(row, col)

    def get_listener(self):
        return self._listener

