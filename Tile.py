import random

import pygame
import os
from Item import *


class Tile:

    def __init__(self):
        self.asset = pygame.image.load(os.path.join("assets", "no_tile_texture.png"))
        self.item = None
        self.dark = pygame.image.load(os.path.join("assets", "dark.png"))
        self.shadow = pygame.image.load(os.path.join("assets", "dim.png"))

    def can_stand(self):
        return False

    def render(self, light_level, window, xoff, yoff, zoom, x, y):
        asset = pygame.transform.scale(self.asset, (int(20 * zoom), int(20 * zoom)))
        window.blit(asset, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
        if light_level == "dim":
            asset1 = pygame.transform.scale(self.shadow, (int(20 * zoom), int(20 * zoom)))
            window.blit(asset1, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
        elif light_level == "bright":
            if self.item is not None:
                self.item.render(window, x, y, zoom, xoff, yoff)

    def is_door(self):
        return False


class FloorTile(Tile):
    def __init__(self, item=None):
        super().__init__()
        self.asset = pygame.image.load(os.path.join("assets", "ground.png"))
        self.item = item

    def can_stand(self):
        return True


class DoorTile(Tile):
    def __init__(self, item=None, locked=False):
        super().__init__()
        self.asset_one = pygame.image.load(os.path.join("assets", "no_tile_texture.png"))
        self.asset_two = pygame.image.load(os.path.join("assets", "no_tile_texture.png"))
        self.asset = self.asset_one
        self.item = item
        self.locked = False

    def can_stand(self):
        return not self.locked

    def is_door(self):
        return True


class DungeonDoorTile(DoorTile):
    def __init__(self, item=None, locked=False):
        super().__init__()
        self.asset_one = pygame.image.load(os.path.join("assets", "dungeon_door.png"))
        self.asset_two = pygame.image.load(os.path.join("assets", "dungeon_door_open.png"))
        self.asset = self.asset_one
        self.item = item
        self.locked = False

    def can_stand(self):
        return not self.locked


class CellDoorTile(DoorTile):
    def __init__(self, item=None, locked=False):
        super().__init__()
        self.asset_one = pygame.image.load(os.path.join("assets", "cell_door.png"))
        self.asset_two = pygame.image.load(os.path.join("assets", "cell_door_open.png"))
        self.asset = self.asset_one
        self.item = item
        self.locked = False

    def can_stand(self):
        return not self.locked


class WallTile(Tile):
    def __init__(self):
        super().__init__()
        num = random.randint(1, 100)
        if num <= 65:
            self.asset = pygame.image.load(os.path.join("assets", "stone_wall_1.png"))
        else:
            self.asset = pygame.image.load(os.path.join("assets", "stone_wall_2.png"))

    def can_stand(self):
        return False


class SecretWallTile(Tile):
    def __init__(self, item=None):
        super().__init__()
        self.asset_one = pygame.image.load(os.path.join("assets", "wall.png"))
        self.asset_two = pygame.image.load(os.path.join("assets", "ground.png"))
        self.asset = self.asset_one
        self.item = item
        self.found = False
        self.neighbours = []

    def can_stand(self):
        return True

    def set_entrance(self):
        self.asset_two = pygame.image.load(os.path.join("assets", "secret_wall_entrance.png"))

    def reveal(self, map):
        if not self.found:
            self.found = True
            self.asset = self.asset_two
            for i in self.neighbours:
                tile = map[i[1]][i[0]]
                if not tile.found:
                    tile.reveal(map)
