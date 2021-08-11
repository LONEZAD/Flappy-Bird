import sys
import pygame

from window_handler import WindowHandler
from event_handler import EventHandler


class Main:
    __window_handler_instance: WindowHandler
    __event_handler_instance: EventHandler

    def __init__(self) -> None:
        self.__window_handler_instance = WindowHandler()
        self.__event_handler_instance = EventHandler()
        self.__event_handler_instance.add_event_callback(pygame.QUIT, self.__window_exit_callback)
        self.__run()

    def __run(self) -> None:
        while True:
            self.__update()
            self.__render()

    def __update(self):
        self.__event_handler_instance.update()

    def __render(self):
        self.__window_handler_instance.pygame_window_surface.fill((0, 0, 0))
        pygame.display.flip()

    @staticmethod
    def __window_exit_callback() -> None:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Main()
