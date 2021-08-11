from game.game_handler import GameHandler


class ApplicationHandler:
    __game_handler: GameHandler

    def __init__(self):
        self.__game_handler = GameHandler()

    def update(self):
        self.__game_handler.update()

    def render(self):
        self.__game_handler.render()
