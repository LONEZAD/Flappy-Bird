from src.game.game_objects.rigid_body import RectangleRigidBody


class Obstacle(RectangleRigidBody):
    def __init__(self) -> None:
        super(Obstacle, self).__init__()
        self._set_image("images/obstacle.png")
        self._set_size([10, 50])
        self._set_velocity([-100, 0])

    def update(self, delta_time: float) -> None:
        super(Obstacle, self).update(delta_time)
        if self._get_position()[0] + self._get_size()[0] / 2 < 0:
            self._set_position([
                100 + self._get_size()[0] / 2,
                self._get_position()[1]
            ])

    @property
    def size(self) -> [float, float]:
        return self._get_size()
