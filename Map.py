from FloorTile import FloorTile
from WallTile import WallTile


class Map:
    def __init__(self, maplist, player):
        self.player = player
        self.map = []
        self.build_map(maplist)

    def build_map(self, maplist):
        for i in range(len(maplist)):
            blank = []
            for e in range(len(maplist[i])):
                if maplist[i][e] == 1:
                    floor = FloorTile()
                    blank.append(floor)
                elif maplist[i][e] == 0:
                    wall = WallTile()
                    blank.append(wall)
            self.map.append(blank)

    def move_player_right(self, num):
        tile = self.map[self.player.y][self.player.x + num]
        if tile.can_stand():
            self.player.x += num

    def move_player_up(self, num):
        tile = self.map[self.player.y + num][self.player.x]
        if tile.can_stand():
            self.player.y += num
