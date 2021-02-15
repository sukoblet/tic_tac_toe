from ui.Drawer import Drawer

import sys
import pygame


class EventsListener:
    def __init__(self, status, handler, fps):
        self._status = status
        self._handler = handler
        self._drawer = Drawer()
        self._fps = fps
        self._translator = None

    def set_translator(self, translator):
        # TODO should we allow setting the translator multiple times?
        self._translator = translator

    def listen_to_move(self):
        if self._translator is None:
            raise ValueError('You must set the translator object before calling this method')

        running = True
        clock = pygame.time.Clock()
        self._status.start_round()  # FIXME fix the method name to the real one
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # TODO hovering effect by taking the position of the mouse and ...

                if event.type == pygame.MOUSEBUTTONUP:
                    self._handler.callback_onclick(event)
                    # TODO the best way would be getting row/column out of x, y, we need some translator

            if self._status.is_round_finished():
                running = False

            clock.tick(self._fps)

        # TODO maybe some actions needed after the round is finished
