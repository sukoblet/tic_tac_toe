import pygame


class GameEngine:
    def __init__(self, game, view, fps):
        self._fps = fps

        self._game = game
        self._view = view
        self._status = game.get_status()

        self._clock = pygame.time.Clock()

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
        if not self._status.is_game:
            self._status.play_game()
        game_scene = self._view.play()
        game_scene.render()
        listener = game_scene.get_listener()

        listener.listen_to_move()

        self._end()

    def _end(self):
        end_scene = self._view.end()
        end_scene.render()

        while True:
            for event in pygame.event.get():
                end_scene.handle_event(event)

                self._clock.tick(self._fps)
