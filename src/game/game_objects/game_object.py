import pygame
from typing import Annotated
from src.window_handler import WindowHandler
from src.event_handler import EventHandler


class GameObject:  # Someone clean this class up!!!
    __image_to_be_drawn: pygame.Surface
    __original_image: pygame.Surface
    __position_percentage: Annotated[list[float], 2]
    __size_percentage: Annotated[list[float], 2]
    __window_handler_instance: WindowHandler

    def __init__(self) -> None:
        self.__window_handler_instance = WindowHandler()
        self.__size_percentage = [50, 50]
        self.__position_percentage = [50, 50]
        self._set_image("default.png")
        event_handler_instance: EventHandler = EventHandler()
        event_handler_instance.add_event_callback(pygame.WINDOWRESIZED, self.__update_image)

    def update(self, delta_time: float) -> None:
        pass

    def render(self) -> None:
        self.__window_handler_instance.pygame_window_surface.blit(self.__image_to_be_drawn, self.__absolute_position)

    @property
    def __absolute_position(self) -> list[int]:
        return [
            int(
                self.__position_percentage[i] *
                self.__window_handler_instance.pygame_window_surface.get_size()[i]
                / 100
                - self.__absolute_size[i] / 2
            ) for i in range(2)
        ]

    @property
    def __absolute_size(self) -> list[int]:
        return [
            int(
                self.__size_percentage[i] * self.__window_handler_instance.pygame_window_surface.get_size()[i] / 100
            ) for i in range(2)
        ]

    def __update_image(self) -> None:
        self.__image_to_be_drawn = pygame.transform.scale(self.__original_image, self.__absolute_size).convert()

    def _set_image(self, path: str) -> None:
        try:
            self.__original_image = pygame.image.load(path).convert()
            self.__update_image()
        except FileNotFoundError:
            raise FileNotFoundError("The file " + path + " was not found.\n" +
                                    "Please make sure that the path is relative to the assets folder")
