import time


class GameHandler:
    __last_time_update_was_called: float

    def __init__(self) -> None:
        self.__last_time_update_was_called = time.time()

    def update(self) -> None:
        delta_time: float
        # Ignore the warning ... this will be used when GameObjects are implemented
        delta_time = time.time() - self.__last_time_update_was_called
        self.__last_time_update_was_called = time.time()

    def render(self) -> None:
        pass

    @property
    def should_game_start(self) -> bool:
        return False  # A dummy return value til the game is made
