from Tile import Tile
import pygame
import os


class FloorTile(Tile):
    def __init__(self, item=None):
        super().__init__()
        self.asset = pygame.image.load(os.path.join("assets", "ground.png"))
        self.item = item

    def can_stand(self):
        return True