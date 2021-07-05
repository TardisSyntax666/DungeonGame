from PIL import Image
import pygame
import os
import time

from Map import Map
from Character import Character

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")

CLOCK = pygame.time.Clock()
FPS = 60
ZOOM = 2.5


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
            elif r == 0 and g == 0 and b == 255:
                map_list[y].append(2)
            elif r == 0 and g == 255 and b == 0:
                map_list[y].append('start')
            else:
                map_list[y].append(1)

    return map_list


def draw_window(gameboard):
    WINDOW.fill((0, 0, 0))

    player = gameboard.player

    map_width = int(len(gameboard.map[0]) * 20 * ZOOM)
    map_height = int(len(gameboard.map) * 20 * ZOOM)
    xvar = player.x * 20 * ZOOM / map_width
    yvar = player.y * 20 * ZOOM / map_height
    xoff = int((map_width - WIDTH) * xvar)
    yoff = int((map_height - 600) * yvar)

    gameboard.render(WINDOW, xoff, yoff, ZOOM)

    player_asset = pygame.transform.scale(player.asset, (int(20 * ZOOM), int(20 * ZOOM)))
    WINDOW.blit(player_asset, (int(player.x * 20 * ZOOM) - xoff, int(player.y * 20 * ZOOM) - yoff))

    pygame.display.update()


def main():
    run = True
    button_list = []
    mapp = load_map("map2.png")
    player_pos = (20, 20)
    move_limit = 10
    move_limiter = 0
    player = Character("character.png", 100)
    game_board = Map(mapp, player)

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
        player = game_board.player
        if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and move_limiter == 0:
            if game_board.map[player.y - 1][player.x].can_stand():
                player.move_up(-1)
            move_limiter += 1
        if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and move_limiter == 0:
            if game_board.map[player.y + 1][player.x].can_stand():
                player.move_up(1)
            move_limiter += 1
        if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and move_limiter == 0:
            if game_board.map[player.y][player.x - 1].can_stand():
                player.move_right(-1)
            move_limiter += 1
        if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and move_limiter == 0:
            if game_board.map[player.y][player.x + 1].can_stand():
                player.move_right(1)
            move_limiter += 1

        draw_window(game_board)
    quit()


if __name__ == "__main__":
    main()
