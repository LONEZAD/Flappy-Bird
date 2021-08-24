from src.game.game_objects.rigid_body import RectangleRigidBody


class ObstacleType:
    UPPER = "upper"
    LOWER = "lower"


class ObstacleConfigurationHelper:
    WIDTH = "width"
    VELOCITY = "velocity"
    TYPE = "type"
    HEIGHT = "height"
    X_POSITION = "x-position"
    IMAGE_PATH = "image-path"


class Obstacle(RectangleRigidBody):
    __defaults: dict = dict()  # A default value in case it is not initialised

    @classmethod
    def set_defaults(cls, defaults: dict) -> None:
        cls.__defaults = defaults

    def __is_defaults_ready(self) -> bool:
        return (
                self.__defaults.get(ObstacleConfigurationHelper.WIDTH) is not None and
                self.__defaults.get(ObstacleConfigurationHelper.VELOCITY) is not None and
                self.__defaults.get(ObstacleConfigurationHelper.IMAGE_PATH) is not None
        )

    def __init__(self, height: float, x_position: float, obstacle_type: ObstacleType) -> None:
        if not self.__is_defaults_ready():
            # TODO:- this should be the python equivalent of IllegalStateException
            raise Exception(f"Defaults are not ready yet. {self.__defaults}")

        super(Obstacle, self).__init__()
        self._set_image(self.__defaults[ObstacleConfigurationHelper.IMAGE_PATH])

        self._set_size([self.__defaults[ObstacleConfigurationHelper.WIDTH], height])
        self._set_velocity([self.__defaults[ObstacleConfigurationHelper.VELOCITY], 0])

        self.__set_type(x_position, obstacle_type)

    def update(self, delta_time: float) -> None:
        super(Obstacle, self).update(delta_time)
        if self._get_position()[0] + self._get_size()[0] / 2 < 0:
            self._set_position([
                100 + self._get_size()[0] / 2,
                self._get_position()[1]
            ])

    def __set_type(self, x_position: float, obstacle_type: ObstacleType) -> None:
        y_position: float
        if obstacle_type == ObstacleType.LOWER:
            y_position = 100 - self._get_size()[1] / 2
        elif obstacle_type == ObstacleType.UPPER:
            y_position = 0 + self._get_size()[1] / 2
        else:
            raise ValueError(f"{obstacle_type} is not a valid obstacle type!!!")
        self._set_position(
            [x_position, y_position]
        )

    @property
    def size(self) -> [float, float]:
        return self._get_size()
