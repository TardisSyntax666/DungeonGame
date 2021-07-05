import os
import pygame
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
    # print(resource)
    return resource


class Item:

    def __init__(self):
        self.asset = pygame.image.load(os.path.join("assets", "no_item_texture.png"))

    def use_item(self):
        pass

    def render(self, window, gameboard, xoff, yoff, zoom, player):
        pass

    def is_bright(self):
        return False


class Torch(Item):

    def __init__(self):
        super().__init__()
        self.asset = pygame.image.load(os.path.join("assets", "torch.png"))
        self.resource = load_reasource("torch_rad.png")

    def use_item(self):
        pass

    def render(self, window, x, y, zoom, xoff, yoff):
        asset = pygame.transform.scale(self.asset, (int(20 * zoom), int(20 * zoom)))
        window.blit(asset, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))

    def is_bright(self):
        return True


class IronSword(Item):

    def __init__(self):
        super().__init__()
        self.asset = pygame.image.load(os.path.join("assets", "iron_sword.png"))

    def use_item(self):
        pass

    def render(self, window, x, y, zoom, xoff, yoff):
        asset = pygame.transform.scale(self.asset, (int(20 * zoom), int(20 * zoom)))
        window.blit(asset, (int(x * 20 * zoom) - xoff, int(y * 20 * zoom) - yoff))
