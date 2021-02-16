# TODO this is only for the program to start, rewrite!!!
from backend.logic.EventsHandler import EventsHandler
from backend.logic.GameStatus import GameStatus


class Game:
    def __init__(self):
        self._status = GameStatus()
        self._handler = EventsHandler()

    def get_status(self):
        return self._status

    def get_events_handler(self):
        return self._handler
