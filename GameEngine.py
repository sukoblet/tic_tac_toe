import sys
import pygame


class GameEngine:
    def __init__(self, game, view, fps):
        self._fps = fps

        self._game = game
        self._view = view
        self._status = game.get_status()

        self._clock = pygame.time.Clock()

    # TODO game engine switches scenes, rounds and so on, it uses APIs from packages to visualise/calculate everything
    def run(self):
        if not self._status.is_initial():
            raise ValueError("The engine is already run, you can't run it again")
        self._start()

    def _start(self):
        self._status.start_game()
        start_scene = self._view.start()
        start_scene.render()

        while self._status.is_start():
            for event in pygame.event.get():
                start_scene.handle_event(event)

            self._clock.tick(self._fps)

        self._play()

    def _play(self):
        self._view.play()

        while self._status.is_game():
            for event in pygame.event.get():  # TODO change this to EventsListener and so on
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._clock.tick(self._fps)

    def _end(self):
        self._view.end()
