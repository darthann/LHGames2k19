from helper.data import *
import numpy as np


def distanceCostTiles(start, end):
    return (start.position.x - end.position.x) ** 2 + (start.position.y - end.position.y) ** 2


def findBestNeighbourTile(game_info):
    current_position = game_info.host_player.position
    current_tile = game_info.map.tiles[current_position.y][current_position.x]

    results = []

    # TODO check if tile is tail
    # If go out of base 1 case distance what is the cost ? (add the come back)

    # LEFT
    for pos in range(current_position.y, 2):
        temp = game_info.map.tiles[pos][current_position.x]
        if temp.is_empty:
            results.append(temp)
            break

    # RIGHT
    for pos in range(current_position.y, 15):
        temp = game_info.map.tiles[pos][current_position.x]
        if temp.is_empty:
            results.append(temp)
            break

    # UP
    for pos in range(current_position.x, 15):
        temp = game_info.map.tiles[current_position.y][pos]
        if temp.is_empty:
            results.append(temp)
            break

    # DOWN
    for pos in range(current_position.x, 2):
        temp = game_info.map.tiles[current_position.y][pos]
        if temp.is_empty:
            results.append(temp)
            break

    if results.__len__() == 1:
        distanceMin = distanceCostTiles(current_tile, results[0])
        tile_min = results[0]
        # TODO Check si le nombre de coup possible est supérieur al a distance totale d'aller retour
        print("Shortest distance is {} from [{}, {}] to [{}, {}]".format(distanceMin, current_tile.position.y, current_tile.position.x, tile_min.position.y, tile_min.position.x))
        if distanceMin == 0:
            return None
        else:
            return tile_min
    elif results.__len__() > 1:
        distanceMin = distanceCostTiles(current_tile, results[0])
        tile_min = results[0]
        for i in range(1, results.__len__()):
            if distanceCostTiles(current_tile, results[i]) < distanceMin:
                distanceMin = distanceCostTiles(current_tile, results[i])
                tile_min = results[i]
        print("Shortest distance is {} from [{}, {}] to [{}, {}]".format(distanceMin, current_tile.position.y, current_tile.position.x, tile_min.position.y, tile_min.position.x))
        if distanceMin == 0:
            return None
        else:
            return tile_min
    else:
        return None


def findDistanceToBase(start):
    return None


# TODO: Rester sur place tant que find neighbours ne retourne pas de bonnes destinations
def stayPut():
   return None


def movementToTile(start, end):
    if start.position.x == end.position.x:
        if start.position.y > end.position.y:
            return Direction.UP
        else:
            return Direction.DOWN
    else:
        if start.position.x > end.position.x:
            return Direction.LEFT
        else:
            return Direction.RIGHT


def movementToPos(start, end):
    if start[0] == end[0]:
        if start[1] > end[1]:
            return Direction.LEFT
        else:
            return Direction.RIGHT
    else:
        if start[0] > end[0]:
            return Direction.UP
        else:
            return Direction.DOWN


def isHome(game_info):
    '''
    Retourne True si le joueur est chez lui
    '''
    current_map = game_info.map.tiles
    current_position = game_info.host_player.position
    team_number = game_info.host_player.team_number
    teamOwner = current_map[current_position.y][current_position.x].team_owner
    return team_number == teamOwner


def findHomeTileDestination(game_info, visited):
    current_position = game_info.host_player.position
    current_tile = game_info.map.tiles[current_position.y][current_position.x]

    territory_tiles = []
    for x in range(15):
        for y in range(15):
            if game_info.map.tiles[y][x].team_owner == game_info.host_player.team_number:
                territory_tiles.append(game_info.map.tiles[y][x])

    temp = tilesAreInVisited(visited, territory_tiles)

    best_tile_to_go_back = temp[0]
    distanceMin = distanceCostTiles(current_tile, temp[0])
    if temp.__len__() > 1:
        for i in range(1, temp.__len__()):
            if distanceMin > distanceCostTiles(current_tile, temp[i]):
                distanceMin = distanceCostTiles(current_tile, temp[i])
                best_tile_to_go_back = temp[i]
    print("Best tile to go home is at distance = {}, position [{}, {}]".format(distanceMin,
                                                                               best_tile_to_go_back.position.y,
                                                                               best_tile_to_go_back.position.x))
    return best_tile_to_go_back


def mapMaker(game_info, visited):
    map_tiles = np.zeros((15, 15), dtype=int).tolist()
    for x in range(15):
        for y in range(15):
            flag = True
            for visit in visited:
                if visit.x == x and visit.y == y:
                    flag = False
            if not flag:
                map_tiles[y][x] = 1

    return map_tiles


def tilesAreInVisited(visited, array):
    temp = []
    for tile in array:
        flag = True
        for visit in visited:
            if visit.x == tile.position.x and visit.y == tile.position.y:
                flag = False
        if flag:
            temp.append(tile)
    return temp
