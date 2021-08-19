import time
from src.game.game_objects.required_game_objects.obstacle.obstacle_handler import ObstacleHandler


class GameHandler:
    __last_time_update_was_called: float
    __obstacle_handler: ObstacleHandler

    def __init__(self) -> None:
        self.__last_time_update_was_called = time.time()
        self.__obstacle_handler = ObstacleHandler()

    def update(self) -> None:
        delta_time: float
        delta_time = time.time() - self.__last_time_update_was_called
        self.__obstacle_handler.update(delta_time)
        self.__last_time_update_was_called = time.time()

    def render(self) -> None:
        self.__obstacle_handler.render()

    @property
    def should_game_start(self) -> bool:
        return False  # A dummy return value til the game is made
