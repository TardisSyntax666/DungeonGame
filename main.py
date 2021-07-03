from PIL import Image
import pygame
import os
import time

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")

CLOCK = pygame.time.Clock()
FPS = 60

GROUND = pygame.image.load(os.path.join("assets", "ground.png")).convert_alpha()
WALL = pygame.image.load(os.path.join("assets", "wall.png")).convert_alpha()
CHARACTER = pygame.image.load(os.path.join("assets", "character.png")).convert_alpha()


def load_map(mapfilename):
    map_list = []
    img = Image.open(os.path.join("assets", mapfilename)).convert('RGB')

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

     #this was for visuallizing when it loads the png and converts it to a list
    # for i in map_list:
    #     str_to_prnt = ""
    #     for e in i:
    #          if e == 0:
    #               str_to_prnt += "⬜"
    #          else:
    #               str_to_prnt += "⬛"
    #     print(str_to_prnt)
    return map_list


def draw_window(mapp, character_pos):
    for i in range(len(mapp)):
        pos = 0
        row = mapp[i]
        for e in row:
            #time.sleep(0.01)
            if e == 0:
                WINDOW.blit(WALL, (pos, (i*20)))
            else:
                WINDOW.blit(GROUND, (pos, (i*20)))
            #print(f"blited at {(pos, (i*20))}")
            pos += 20
    WINDOW.blit(CHARACTER, character_pos)
    pygame.display.update()


def main():
    run = True
    button_list = []
    mapp = load_map("map1.png")
    player_pos = (20, 20)

    while run:
        CLOCK.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print("yesy")
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print(1)
                    player_pos = (player_pos[0], player_pos[1] - 20)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_pos = (player_pos[0], player_pos[1] + 20)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_pos = (player_pos[0] - 20, player_pos[1])
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_pos = (player_pos[0] + 20, player_pos[1])

        draw_window(mapp, player_pos)
    quit()


if __name__ == "__main__":
    main()
