from typing import Callable

import pygame.event
from singleton_decorator import singleton


@singleton
class EventHandler:
    __event_callbacks: dict[
        int,
        list[Callable[[], None]]
    ]

    def __init__(self):
        self.__event_callbacks = dict()

    def add_event_callback(self, event: int, callback: Callable[[], None]):
        if self.__event_callbacks.get(event) is None:
            self.__event_callbacks[event] = []
        self.__event_callbacks[event].append(callback)

    def update(self):
        for event in pygame.event.get():
            if self.__event_callbacks.get(event.type) is not None:
                for callback in self.__event_callbacks[event.type]:
                    callback()
