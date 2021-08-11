from game.game_handler import GameHandler
from src.menu.menu_handler import MenuHandler
from typing import Union


class ApplicationHandler:
    __game_handler: Union[GameHandler, None]
    __menu_handler: Union[MenuHandler, None]

    def __init__(self) -> None:
        self.__end_game()

    def __start_game(self) -> None:
        self.__game_handler = GameHandler()
        self.__menu_handler = None

    def __end_game(self) -> None:
        self.__game_handler = None
        self.__menu_handler = MenuHandler()

    def update(self) -> None:
        if self.__game_handler is not None:
            self.__game_handler.update()
            if self.__game_handler.should_game_start:
                self.__end_game()
        if self.__menu_handler is not None:
            self.__menu_handler.update()
            if self.__menu_handler.should_game_start:
                self.__start_game()

    def render(self) -> None:
        if self.__game_handler is not None:
            self.__game_handler.render()
        if self.__menu_handler is not None:
            self.__menu_handler.render()
