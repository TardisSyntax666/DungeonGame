import pygame
import os


class Tile:

    def __init__(self):
        self.asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        self.item = False

    def can_stand(self):
        return False
