from backend.Game import Game
from ui.View import View
from GameEngine import GameEngine


class App:
    def __init__(self):
        self._game = Game()
        self._view = View(self._game)
        self._engine = GameEngine(self._game, self._view)

    def run(self):
        self._engine.run()
