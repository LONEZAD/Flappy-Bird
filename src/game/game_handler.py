import time


class GameHandler:
    __last_time_update_was_called: float

    def __init__(self):
        self.__last_time_update_was_called = time.time()

    def update(self):
        delta_time: float
        # Ignore the warning ... this will be used when GameObjects are implemented
        delta_time = time.time() - self.__last_time_update_was_called
        self.__last_time_update_was_called = time.time()

    def render(self):
        pass
