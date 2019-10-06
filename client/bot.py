from helper.data import *
import bot_calc
from state import State
from helper.app import Settings
import astart


class Bot(object):
    # Code here
    current_state = 0
    limit_movement = 6

    def __init__(self):
        self.steps = 2
        self.visited = []

    """
    GAME_info
        self.__map = map
        self.__host_player = host
        self.__other_players = others
    """

    def get_next_action(self, game_info):
        current_position = game_info.host_player.position
        current_tile = game_info.map.tiles[current_position.y][current_position.x]

        print("Bot current position => [{}, {}]".format(current_position.y, current_position.x))
        if current_position not in self.visited:
            self.visited.append(current_position)

        # Find close tail
        tp = bot_calc.closestTail(game_info)
        if tp is not None:
            print("Enemy tail found close ! => [{}, {}]".format(tp.position.y, tp.position.x))
            move = bot_calc.movementToTile(current_tile, tp)
            print(move)
            return move

        if bot_calc.isHome(game_info):
            self.visited = [current_position]
            destination = bot_calc.findBestNeighbourTile(game_info)
            if destination is not None:
                move = bot_calc.movementToTile(current_tile, destination)
                print(move)
                return move
            # else:
            # TODO Stay put
        else:
            # TODO GO BACK HOME
            destination = bot_calc.findHomeTileDestination(game_info, self.visited)
            start = (game_info.host_player.position.y, game_info.host_player.position.x)
            end = (destination.position.y, destination.position.x)
            map_bin = bot_calc.mapMaker(game_info, self.visited)
            path = astart.astar(map_bin, start, end)
            if path.__len__() > 1:
                move = bot_calc.movementToPos((current_position.y, current_position.x), path[1])
                print("Bot destination => [{}, {}]".format(path[1][0], path[1][1]))
            elif path.__len__() == 1:
                # [(11, 5), (12, 5), (12, 4)]
                move = bot_calc.movementToPos((current_position.y, current_position.x), path[0])
                print("Bot destination (len is 1) => [{}, {}]".format(path[0][0], path[0][1]))

            print(move)

            return move
