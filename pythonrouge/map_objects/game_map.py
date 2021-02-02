from map_objects.tile import Tile
from map_objects.rect import Rect
import random

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(bool(random.getrandbits(1))) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False

def cellular_auto(GM, map_width, map_height):
    for y in range(GM.height):
        CA = 0
        if (y > 2 and y < map_height - 2):
            for x in range(GM.width):
                if (x > 2 and map_width - 2):
                    if GM.tiles[x+1][y-1].blocked == False:
                        CA += 1
                    if GM.tiles[x-1][y-1].blocked == False:
                        CA += 1
                    if GM.tiles[x][y-1].blocked == False:
                        CA += 1
                    if GM.tiles[x+1][y].blocked == False:
                        CA += 1
                    if GM.tiles[x-1][y].blocked == False:
                        CA += 1
                    if GM.tiles[x+1][y+1].blocked == False:
                        CA += 1
                    if GM.tiles[x-1][y+1].blocked == False:
                        CA += 1
                    if GM.tiles[x][y+1].blocked == False:
                        CA += 1
                    if CA < 4:
                        GM.tiles[x][y].blocked == True
    return 