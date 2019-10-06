import numpy as np
import math
import copy
class State:
    
    """
    Contructeur d'un état initial
    """
    def __init__(self, game_info, direction, distance=0):
        self.gameInfo = game_info
        self.direction = direction
        self.distance = distance
        #self.player.position
    """
    GAME_info
        self.__map = map
        self.__host_player = host
        self.__other_players = others
    """

    """
    Estimation du score du coup 
    """
    def estimee(self):
        # TODO
        return  0

    def __hash__(self):
        h = 0
        return int(h)
    
    def __lt__(self, other):
        return 0