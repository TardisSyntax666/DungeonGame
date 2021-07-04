from Tile import Tile
import pygame
import os


class WallTile(Tile):
    def __init__(self):
        super().__init__()
        self.asset = pygame.image.load(os.path.join("assets", "wall.png"))

    def can_stand(self):
        return False