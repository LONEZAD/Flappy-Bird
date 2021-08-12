import pygame
from typing import Annotated
from src.window_handler import WindowHandler


class GameObject:  # Someone clean this class up!!!
    __image_to_be_drawn: pygame.Surface
    __original_image: pygame.Surface
    __position_percentage: Annotated[list[float], 2]
    __size_percentage: Annotated[list[float], 2]
    __window_handler: WindowHandler

    def __init__(self) -> None:
        self.__window_handler = WindowHandler()
        self.__original_image = pygame.image.load("default.png").convert()
        self.__size_percentage = [50, 50]
        self.__position_percentage = [50, 50]
        self.__update_image()

    def update(self, delta_time: float) -> None:
        self.__update_image()  # This will be optimised later

    def render(self) -> None:
        self.__window_handler.pygame_window_surface.blit(self.__image_to_be_drawn, self.__absolute_position)

    @property
    def __absolute_position(self) -> list[int]:
        return [
            int(
                self.__position_percentage[i] *
                self.__window_handler.pygame_window_surface.get_size()[i]
                / 100
                - self.__absolute_size[i] / 2
            ) for i in range(2)
        ]

    @property
    def __absolute_size(self) -> list[int]:
        return [
            int(
                self.__size_percentage[i] * self.__window_handler.pygame_window_surface.get_size()[i] / 100
            ) for i in range(2)
        ]

    def __update_image(self) -> None:
        self.__image_to_be_drawn = pygame.transform.scale(self.__original_image, self.__absolute_size).convert()
