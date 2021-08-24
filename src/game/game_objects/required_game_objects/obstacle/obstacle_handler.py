import json
from src.game.game_objects.required_game_objects.obstacle.obstacle import Obstacle, ObstacleConfigurationHelper


class ObstacleHandler:
    __obstacles: list[Obstacle]

    def __init__(self) -> None:
        self.__initialise_obstacles()

    def __initialise_obstacles(self) -> None:
        Obstacle.set_defaults(self.__get_obstacle_defaults())
        self.__obstacles = self.__generate_obstacles(self.__get_obstacle_configurations())

    @staticmethod
    def __get_obstacle_defaults() -> dict:
        with open("configurations/obstacle_defaults.json") as obstacle_defaults_file:
            return json.load(obstacle_defaults_file)

    @staticmethod
    def __get_obstacle_configurations() -> list[dict]:
        with open("configurations/obstacle_configuration.json") as obstacle_configuration_file:
            return json.load(obstacle_configuration_file)

    @staticmethod
    def __generate_obstacles(obstacle_configurations: list[dict]) -> list[Obstacle]:
        obstacles = list()
        for obstacle_configuration in obstacle_configurations:
            obstacles.append(Obstacle(
                height=10,
                x_position=obstacle_configuration[ObstacleConfigurationHelper.X_POSITION],
                obstacle_type=obstacle_configuration[ObstacleConfigurationHelper.TYPE]
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
