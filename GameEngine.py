class GameEngine:
    def __init__(self, game, view):
        self._game = game
        self._view = view

    # TODO game engine switches scenes, rounds and so on, it uses APIs from packages to visualise/calculate everything
    def run(self):
        self._game.start_game()
        self._view.start()
