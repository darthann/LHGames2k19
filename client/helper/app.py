from os import environ
from helper.singleton import Singleton

class Settings(metaclass=Singleton):
    def __init__(self):
        if "LHAPI_URL" in environ:
            self.__lhapi_url = environ["LHAPI_URL"]
        else:
            self.__lhapi_url = None
        print(f"LHAPI_URL: {self.__lhapi_url}")

        if "GAME_SERVER_URL" in environ:
            self.__game_server_url = environ["GAME_SERVER_URL"]
        else:
            self.__game_server_url = "ws://localhost:5001"

        self.__team_id = 0
        if "TEAM_ID" in environ:
            self.__team_id = environ["TEAM_ID"]
        else:
            self.__team_id = 1

        if "GAME_ID" in environ:
            self.__game_id = environ["GAME_ID"]
        else:
            self.__game_id = 1

    @property
    def lhapi_url(self):
        return self.__lhapi_url

    @property
    def game_server_url(self):
        return self.__game_server_url

    @property
    def team_id(self):
        return self.__team_id

    @property
    def game_id(self):
        return self.__game_id

    @game_server_url.setter
    def game_server_url(self, url):
        self.__game_server_url = url
