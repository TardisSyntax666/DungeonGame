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
                        if (len(self.game_map[0]) > (i[1]+self.player.x) > -1) and (len(self.game_map) > (i[2]+self.player.y) > -1):
                            x, y = (i[1]+self.player.x, i[2]+self.player.y)
                            quords_to_load.append((i[0], x, y))
        if not found_one:
            for i in self.player.default_resource:
                if (len(self.game_map[0]) > (i[1]+self.player.x) > -1) and (len(self.game_map) > (i[2]+self.player.y) > -1):
                    x, y = (i[1]+self.player.x, i[2]+self.player.y)
                    quords_to_load.append((i[0], x, y))
        quords_to_load.append(('bright', self.player.x, self.player.y))
        for i in quords_to_load:
            self.game_map[i[2]][i[1]].render(i[0], window, self, xoff, yoff, zoom, self.player, i[1], i[2])

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
                    door = DungeonDoor()
                    blank.append(door)

                elif maplist[i][e] == 5:
                    door = CellDoor()
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

