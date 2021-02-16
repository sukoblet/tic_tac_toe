from backend.Game import Game
from ui.View import View
from GameEngine import GameEngine


class App:
    def __init__(self):
        self._FPS = 30

        self._game = Game()
        self._view = View(self._game, self._FPS)
        self._engine = GameEngine(self._game, self._view, self._FPS)

    def run(self):
        self._engine.run()
