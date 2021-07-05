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

    def render(self, window, gameboard, xoff, yoff, zoom, player, x, y):
        pass


class FloorTile(Tile):
    def __init__(self, item=None):
        super().__init__()
        self.asset = pygame.image.load(os.path.join("assets", "ground.png"))
        self.item = item

    def can_stand(self):
        return True

    def render(self, window, gameboard, xoff, yoff, zoom, player, x, y):
        asset = pygame.transform.scale(self.asset, (int(20 * zoom), int(20 * zoom)))
        window.blit(asset, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
        item = player.inventory["item"]
        if type(item) is Torch:
            if ('dim', x - player.x, y - player.y) in item.resource:
                asset1 = pygame.transform.scale(self.shadow, (int(20 * zoom), int(20 * zoom)))
                window.blit(asset1, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
            elif ('bright', x - player.x, y - player.y) in item.resource or (x - player.x, y - player.y) == (0, 0):
                if self.item is not None:
                    self.item.render(window, x, y, zoom, xoff, yoff)
            else:
                asset2 = pygame.transform.scale(self.dark, (int(20 * zoom), int(20 * zoom)))
                window.blit(asset2, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))


class WallTile(Tile):
    def __init__(self):
        super().__init__()
        self.asset = pygame.image.load(os.path.join("assets", "wall.png"))

    def can_stand(self):
        return False

    def render(self, window, gameboard, xoff, yoff, zoom, player, x, y):
        asset = pygame.transform.scale(self.asset, (int(20 * zoom), int(20 * zoom)))
        window.blit(asset, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
        item = player.inventory["item"]
        if type(item) is Torch:
            if ('dim', x - player.x, y - player.y) in item.resource:
                asset1 = pygame.transform.scale(self.shadow, (int(20 * zoom), int(20 * zoom)))
                window.blit(asset1, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
            elif ('bright', x - player.x, y - player.y) in item.resource:
                pass
            else:
                asset2 = pygame.transform.scale(self.dark, (int(20 * zoom), int(20 * zoom)))
                window.blit(asset2, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
