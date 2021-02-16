# TODO this is only for the program to start, rewrite!!!
from backend.logic.GameStatus import GameStatus


class Game:
    def __init__(self):
        self._status = GameStatus()

    def get_status(self):
        return self._status

    def get_events_handler(self):
        return None
