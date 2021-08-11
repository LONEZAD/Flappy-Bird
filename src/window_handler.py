import pygame
from singleton_decorator import singleton


@singleton
class WindowHandler:
    __pygame_window_surface: pygame.Surface

    def __init__(self) -> None:
        pygame.init()
        self.__pygame_window_surface = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    @property
    def pygame_window_surface(self) -> pygame.Surface:
        return self.__pygame_window_surface
