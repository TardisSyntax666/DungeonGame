import pygame
import os
from Item import Torch
from PIL import Image

def load_reasource(mapfilename):
    map_list = []
    img = Image.open(os.path.join("assets", mapfilename)).convert('RGB')

    imgpxls = img.load()

    for i in range(img.size[1]):
        map_list.append([])

    player_pos = (0, 0)

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = imgpxls[x, y]
            if r == 255 and g == 255 and b == 255:
                map_list[y].append(0)
            elif r == 100 and g == 100 and b == 100:
                map_list[y].append(2)
            elif r == 0 and g == 0 and b == 255:
                map_list[y].append('player')
                player_pos = (x, y)
            else:
                map_list[y].append(1)

    resource = []

    for y in range(len(map_list)):
        for x in range(len(map_list[y])):
            if map_list[y][x] == 1:
                resource.append(('bright', x - player_pos[0], y - player_pos[1]))
            elif map_list[y][x] == 2:
                resource.append(('dim', x - player_pos[0], y - player_pos[1]))
            else:
                pass
    #print(resource)
    return resource


class Character:
    def __init__(self, asset, health, inventory=None):
        self.x = 1
        self.y = 1
        self.asset = pygame.image.load(os.path.join("assets", asset))
        self.health = health
        self.default_resource = load_reasource("default_rad.png")
        if inventory is None:
            self.inventory = {'item': Torch(), 'magic': None, 'weapon': None, 'armour': None}
        else:
            self.inventory = inventory

    def move_right(self, num):
        self.x += num

    def move_up(self, num):
        self.y += num
