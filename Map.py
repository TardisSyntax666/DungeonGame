from Tile import *
from Item import *


class Map:
    def __init__(self, maplist, player):
        self.player = player
        self.game_map = []
        self.build_map(maplist)

    def render(self, window, xoff, yoff, zoom):
        inv = self.player.inventory
        quords_to_load = []
        found_one = False
        for e in inv.items():
            if e[1] is not None:
                if e[1].is_bright():
                    found_one = True
                    for i in e[1].resource:
                        if (len(self.game_map[0]) > (i[1] + self.player.x) > -1) and (
                                len(self.game_map) > (i[2] + self.player.y) > -1):
                            x, y = (i[1] + self.player.x, i[2] + self.player.y)
                            quords_to_load.append((i[0], x, y))
        if not found_one:
            for i in self.player.default_resource:
                if (len(self.game_map[0]) > (i[1] + self.player.x) > -1) and (
                        len(self.game_map) > (i[2] + self.player.y) > -1):
                    x, y = (i[1] + self.player.x, i[2] + self.player.y)
                    quords_to_load.append((i[0], x, y))
        quords_to_load.append(('bright', self.player.x, self.player.y))
        for i in quords_to_load:
            self.game_map[i[2]][i[1]].render(i[0], window, xoff, yoff, zoom, i[1], i[2])

    def build_map(self, maplist):
        for i in range(len(maplist)):
            blank = []
            for e in range(len(maplist[i])):

                if maplist[i][e] == 1:
                    floor = FloorTile()
                    blank.append(floor)

                elif maplist[i][e] == 2:
                    sword = IronSword()
                    floor = FloorTile(sword)
                    blank.append(floor)

                elif maplist[i][e] == 3:
                    floor = SecretWallTile()
                    blank.append(floor)

                elif maplist[i][e] == 4:
                    door = DungeonDoorTile()
                    blank.append(door)

                elif maplist[i][e] == 5:
                    door = CellDoorTile()
                    blank.append(door)

                elif maplist[i][e] == 'spawn':
                    floor = FloorTile()
                    self.player.x = e
                    self.player.y = i
                    blank.append(floor)

                elif maplist[i][e] == 0:
                    wall = WallTile()
                    blank.append(wall)

            self.game_map.append(blank)
        temp = []
        #print(self.game_map)
        for y in range(len(self.game_map)):
            blank = []
            for x in range(len(self.game_map[y])):
                quords = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
                tile = self.game_map[y][x]
                if type(tile) == SecretWallTile:
                    if not (x == 0 or y == 0 or x == len(self.game_map[0]) or y == len(self.game_map)):
                        for q in quords:
                            in_question = self.game_map[q[1]][q[0]]
                            if type(in_question) == FloorTile:
                                tile.set_entrance()
                            elif type(in_question) == SecretWallTile:
                                if not((x, y) in in_question.neighbours):
                                    in_question.neighbours.append((x, y))
                blank.append(tile)
            temp.append(blank)
        self.game_map = temp
