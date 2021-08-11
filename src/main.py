import sys
import pygame.event
from window_handler import WindowHandler


class Main:
    __window_handler_instance: WindowHandler

    def __init__(self) -> None:
        self.__window_handler_instance = WindowHandler()
        self.__run()

    def __run(self) -> None:
        while True:
            self.__handle_events()
            self.__update()
            self.__render()

    def __handle_events(self) -> None:  # TODO: Remove this and replace it with a permanent EventHandler
        """
        A temporary implementation till we have a proper event handler
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__window_exit_callback()

    def __update(self):
        pass

    def __render(self):
        self.__window_handler_instance.pygame_window_surface.fill((0, 0, 0))
        pygame.display.flip()

    @staticmethod
    def __window_exit_callback() -> None:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Main()
