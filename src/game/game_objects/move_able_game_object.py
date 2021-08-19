from typing import Annotated

from src.game.game_objects.game_object import GameObject


class MoveAbleGameObject(GameObject):
    __velocity_percentage: Annotated[list[float], 2]
    __acceleration_percentage: Annotated[list[float], 2]

    def __init__(self):
        super().__init__()
        self._set_image("images/move_able_default.png")
        # self.__velocity_percentage = [10, 10]
        self.__velocity_percentage = [0, 0]
        self.__acceleration_percentage = [0, 0]
        # self._translate([10, 10])

    def update(self, delta_time: float) -> None:
        super().update(delta_time)
        for i in range(2):
            self.__velocity_percentage[i] += self.__acceleration_percentage[i] * delta_time
        self._set_position([
            self._get_position()[i] + self.__velocity_percentage[i] * delta_time
            for i in range(2)
        ])

    def _translate(self, displacement_percentage: Annotated[list[float], 2]) -> None:
        self._set_position([
            self._get_position()[i] + displacement_percentage[i]
            for i in range(2)
        ])

    def _set_velocity(self, velocity_percentage: Annotated[list[float], 2]) -> None:
        self.__velocity_percentage = velocity_percentage

    def _get_velocity(self) -> Annotated[list[float], 2]:
        return self.__velocity_percentage

    def _set_acceleration(self, acceleration_percentage: Annotated[list[float], 2]) -> None:
        self.__acceleration_percentage = acceleration_percentage

    def _get_acceleration_percentage(self) -> Annotated[list[float], 2]:
        return self.__acceleration_percentage
