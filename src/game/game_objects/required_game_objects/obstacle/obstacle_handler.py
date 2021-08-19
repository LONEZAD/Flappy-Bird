from src.game.game_objects.required_game_objects.obstacle.obstacle import Obstacle, ObstacleType, \
    ObstacleConfigurationHelper


class ObstacleHandler:
    __obstacles: list[Obstacle]

    def __init__(self) -> None:
        self.__initialise_obstacles()

    def __initialise_obstacles(self) -> None:
        Obstacle.set_defaults(self.__get_obstacle_defaults())
        self.__obstacles = self.__generate_obstacles(self.__get_obstacle_configurations())

    @staticmethod
    def __get_obstacle_defaults() -> dict:
        # TODO:- Refactor this to a config file
        # A dummy configuration till we have a real config file
        return {
            ObstacleConfigurationHelper.WIDTH: 50,
            ObstacleConfigurationHelper.VELOCITY: -100
        }

    @staticmethod
    def __get_obstacle_configurations() -> list[dict]:
        # TODO:- Refactor this to a config file
        # A dummy configuration till we have a real config file
        return [
            {
                ObstacleConfigurationHelper.TYPE: ObstacleType.LOWER,
                ObstacleConfigurationHelper.X_POSITION: 10
            },
            {
                ObstacleConfigurationHelper.TYPE: ObstacleType.UPPER,
                ObstacleConfigurationHelper.X_POSITION: 10
            }
        ]

    @staticmethod
    def __generate_obstacles(obstacle_configurations: list[dict]) -> list[Obstacle]:
        obstacles: list[Obstacle]
        obstacles = list()
        for obstacle_configuration in obstacle_configurations:
            obstacles.append(Obstacle(
                10,
                obstacle_configuration[ObstacleConfigurationHelper.X_POSITION],
                obstacle_configuration[ObstacleConfigurationHelper.TYPE]
            ))
        return obstacles

    def update(self, delta_time: float) -> None:
        obstacle: Obstacle
        for obstacle in self.__obstacles:
            obstacle.update(delta_time)

    def render(self) -> None:
        obstacle: Obstacle
        for obstacle in self.__obstacles:
            obstacle.render()
