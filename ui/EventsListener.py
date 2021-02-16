from ui.Drawer import Drawer

import sys
import pygame


class EventsListener:
    def __init__(self, status, handler, fps, translator):
        if status is None:
            raise ValueError('You cannot transfer status as None to the constructor')
        if handler is None:
            raise ValueError('You cannot transfer handler as None to the constructor')
        if translator is None:
            raise ValueError('You cannot transfer translator as None to the constructor')
        if fps <= 0:
            raise ValueError('FPS must be a positive number')

        self._status = status
        self._handler = handler
        self._drawer = Drawer()
        self._fps = fps
        self._translator = translator

    def listen_to_move(self):
        clock = pygame.time.Clock()
        self._status.start_round()
        while self._status.is_round_active():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # TODO hovering effect by taking the position of the mouse and ...

                if event.type == pygame.MOUSEBUTTONUP:
                    self._handler.callback_onclick(event)
                    # TODO the best way would be getting row/column out of x, y, we need some translator

            clock.tick(self._fps)

        # TODO maybe some actions needed after the round is finished
