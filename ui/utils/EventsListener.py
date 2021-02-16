import sys
import pygame


class EventsListener:
    def __init__(self, status, handler, fps, translator, game_scene):
        if status is None:
            raise ValueError('You cannot transfer status as None to the constructor')
        if handler is None:
            raise ValueError('You cannot transfer handler as None to the constructor')
        if translator is None:
            raise ValueError('You cannot transfer translator as None to the constructor')
        if game_scene is None:
            raise ValueError('You cannot transfer game_scene as None to the constructor')
        if not isinstance(fps, int) or fps <= 0:
            raise ValueError('FPS must be a positive number')

        self._status = status
        self._handler = handler
        self._fps = fps
        self._translator = translator
        self._game_scene = game_scene

    def listen_to_move(self):
        clock = pygame.time.Clock()
        while self._status.is_game():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # TODO hovering effect by taking the position of the mouse and ...

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    rc = self._translator.to_row_column(x, y)
                    if rc is not None:
                        row, col = rc
                        self._handler.callback_onclick(row, col)
                        self._game_scene.render_board_state(row, col)

            clock.tick(self._fps)
