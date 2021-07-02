from PIL import Image
import pygame

WIDTH, HEIGHT = 520, 440
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")


def load_map(mapfilename):
    map_list = []
    img = Image.open(mapfilename).convert('RGB')

    imgpxls = img.load()

    for i in range(img.size[1]):
        map_list.append([])

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = imgpxls[x, y]
            if r == 255 and g == 255 and b == 255:
                map_list[y].append(0)
            else:
                map_list[y].append(1)

    # this was for visuallizing when it loads the png and converts it to a list
    # for i in map_list:
    #    str_to_prnt = ""
    #    for e in i:
    #         if e == 0:
    #              str_to_prnt += "⬜"
    #         else:
    #              str_to_prnt += "⬛"
    #    print(str_to_prnt)
    return map_list

def draw_window():
    pass
