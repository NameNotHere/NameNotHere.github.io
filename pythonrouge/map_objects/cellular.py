from map_objects.game_map import GameMap 

def cellular_auto(GM, map_width, map_height, tt):
    gm = GM
    for y in range(map_height):
        CA = 0
        if (y > 2 and y < map_height - 2):
            for x in range(map_width):
                if (x > 2 and x < map_width - 2):
                    if gm[x+1][y-1].blocked == False:
                        CA += 1
                    if gm[x-1][y-1].blocked == False:
                        CA += 1
                    if gm[x][y-1].blocked == False:
                        CA += 1
                    if gm[x+1][y].blocked == False:
                        CA += 1
                    if gm[x-1][y].blocked == False:
                        CA += 1
                    if gm[x+1][y+1].blocked == False:
                        CA += 1
                    if gm[x-1][y+1].blocked == False:
                        CA += 1
                    if gm[x][y+1].blocked == False:
                        CA += 1
                gm[x][y].blocked = True
                gm[x][y].blocked_sight = True
    return GameMap(map_width, map_height)