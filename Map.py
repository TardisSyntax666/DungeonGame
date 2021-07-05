from Tile import FloorTile, WallTile
from Item import IronSword


class Map:
    def __init__(self, maplist, player):
        self.player = player
        self.map = []
        self.build_map(maplist)

    def render(self, window, xoff, yoff, zoom):
        for i in range(len(self.map)):
            for e in range(len(self.map[i])):
                self.map[i][e].render(window, self, xoff, yoff, zoom, self.player, e, i)

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

                elif maplist[i][e] == 'start':
                    floor = FloorTile()
                    self.player.x = e
                    self.player.y = i
                    blank.append(floor)

                elif maplist[i][e] == 0:
                    wall = WallTile()
                    blank.append(wall)

            self.map.append(blank)

