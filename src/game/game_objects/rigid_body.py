from abc import ABC, abstractmethod
from src.game.game_objects.move_able_game_object import MoveAbleGameObject


class RectangleRigidBody(MoveAbleGameObject, ABC):
    @property
    @abstractmethod
    def size(self) -> [float, float]:
        """Should return the width, height"""


class CircularRigidBody(MoveAbleGameObject, ABC):
    def __init__(self):
        super().__init__()
        self._set_image("images/circle_default.png")

    @property
    @abstractmethod
    def radius(self) -> float:
        """Should return the """
