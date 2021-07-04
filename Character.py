import pygame
import os


class Character:
    def __init__(self, asset):
        self.x = 1
        self.y = 1
        self.asset = pygame.image.load(os.path.join("assets", asset))

