from PIL import Image
import pygame
import os
import time

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")

CLOCK = pygame.time.Clock()
FPS = 60
ZOOM = 2

GROUND = pygame.image.load(os.path.join("assets", "ground.png")).convert_alpha()
GROUND = pygame.transform.scale(GROUND, (int(GROUND.get_rect().width*ZOOM), int(GROUND.get_rect().height*ZOOM)))
WALL = pygame.image.load(os.path.join("assets", "wall.png")).convert_alpha()
WALL = pygame.transform.scale(WALL, (int(WALL.get_rect().width*ZOOM), int(WALL.get_rect().height*ZOOM)))
CHARACTER = pygame.image.load(os.path.join("assets", "character.png")).convert_alpha()
CHARACTER = pygame.transform.scale(CHARACTER, (int(CHARACTER.get_rect().width*ZOOM), int(CHARACTER.get_rect().height*ZOOM)))


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
    mapsize = (int(len(mapp[0])*20*ZOOM)), int(len(mapp)*20*ZOOM)
    if 1001 > character_pos[0] > -1 and 801 > character_pos[1] > -1:
        x_var = 500 - character_pos[0]
        y_var = 400 - character_pos[1]
        #x_var = 500 - 0
        #y_var = 400 - 0
        if x_var >= 500:
            offx = int((x_var-500)/500*(1000-mapsize[0]))*-1
        else:
            offx = int(x_var / 500 * (1000 - mapsize[0]))*-1
        if y_var >= 400:
            offy = int((y_var - 400) / 400 * (1000 - mapsize[1]))
        else:
            offy = int(y_var / 400 * (1000 - mapsize[1]))
    else:
        offx = 0
        offy = 0

    for i in range(len(mapp)):
        pos = 0
        row = mapp[i]
        for e in row:
            #time.sleep(0.01)
            if e == 0:
                WINDOW.blit(WALL, (int(pos*ZOOM)+offx, int(i*20*ZOOM)+offy))
            else:
                WINDOW.blit(GROUND, (int(pos*ZOOM)+offx, int(i*20*ZOOM)+offy))
            #print(f"blited at {(pos, (i*20))}")
            pos += 20
    WINDOW.blit(CHARACTER, (int(character_pos[0]*ZOOM)+offx, int(character_pos[1]*ZOOM)+offy))
    pygame.display.update()


def main():
    run = True
    button_list = []
    mapp = load_map("map1.png")
    player_pos = (20, 20)
    move_limit = 15
    move_limiter = 0

    while run:
        CLOCK.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if move_limiter != 0:
            if move_limiter == move_limit:
                move_limiter = 0
            else:
                move_limiter += 1

        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and move_limiter == 0:
            player_pos = (player_pos[0], player_pos[1] - 20)
            move_limiter += 1
        if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and move_limiter == 0:
            player_pos = (player_pos[0], player_pos[1] + 20)
            move_limiter += 1
        if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and move_limiter == 0:
            player_pos = (player_pos[0] - 20, player_pos[1])
            move_limiter += 1
        if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and move_limiter == 0:
            player_pos = (player_pos[0] + 20, player_pos[1])
            move_limiter += 1


        draw_window(mapp, player_pos)
    quit()


if __name__ == "__main__":
    main()
