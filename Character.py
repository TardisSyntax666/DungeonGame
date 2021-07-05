import pygame
import os
from Item import Torch


class Character:
    def __init__(self, asset, health, inventory=None):
        self.x = 1
        self.y = 1
        self.asset = pygame.image.load(os.path.join("assets", asset))
        self.health = health
        if inventory is None:
            self.inventory = {'item': Torch(), 'magic': None, 'weapon': None, 'armour': None}
        else:
            self.inventory = inventory

    def move_right(self, num):
        self.x += num

    def move_up(self, num):
        self.y += num
