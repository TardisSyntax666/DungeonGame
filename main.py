from PIL import Image
import pygame
import os
import time

from Tile import *
from Map import Map
from Character import Character
from UI import *

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")

CLOCK = pygame.time.Clock()
FPS = 60
ZOOM = 3


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
            elif r == 50 and g == 50 and b == 50:
                map_list[y].append(3)
            elif r == 255 and g == 0 and b == 0:
                map_list[y].append(4)
            elif r == 200 and g == 0 and b == 0:
                map_list[y].append(5)
            elif r == 0 and g == 255 and b == 0:
                map_list[y].append('spawn')
            else:
                map_list[y].append(1)

    return map_list


def draw_window(gameboard, stats_board):
    WINDOW.fill((0, 0, 0))

    player = gameboard.player

    map_width = len(gameboard.game_map[0]) * 20 * ZOOM
    map_height = len(gameboard.game_map) * 20 * ZOOM
    xvar = player.x * 20 * ZOOM / map_width
    yvar = player.y * 20 * ZOOM / map_height
    xoff = int((map_width - WIDTH + 600) * xvar) - 300
    yoff = int((map_height - HEIGHT + 600) * yvar) - 300

    gameboard.render(WINDOW, xoff, yoff, ZOOM)
    stats_board.render(WINDOW, (200, 700))

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
    changed_tiles = []
    stats_board = StatsUI(player.inventory)

    while run:
        CLOCK.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)
        keys_pressed = pygame.key.get_pressed()
        player = game_board.player
        current_tile = game_board.game_map[player.y][player.x]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in stats_board.inv_buttons.items():
                    if i[1].is_over(pos):
                        if i[1].selected:
                            i[1].selected = False
                        else:
                            i[1].select()
                for i in stats_board.buttons.items():
                    if i[1].is_over(pos) and not i[1].locked:
                        i[1].selected = True

                button = stats_board.buttons["drop"]
                select = stats_board.get_selected_invbutton()
                if button.is_over(pos) and not button.locked:
                    current_tile.item = select.item
                    player.inventory[current_tile.item.type] = None
                    stats_board.update_inventory(player.inventory)

                button = stats_board.buttons["pickup"]
                select = stats_board.get_selected_invbutton()
                if button.is_over(pos) and not button.locked:
                    player.inventory[current_tile.item.type] = current_tile.item
                    current_tile.item = None
                    stats_board.update_inventory(player.inventory)

            if event.type == pygame.KEYDOWN:

                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    if event.key == pygame.K_1:
                        button = stats_board.inv_buttons['item']
                    elif event.key == pygame.K_2:
                        button = stats_board.inv_buttons['magic']
                    elif event.key == pygame.K_3:
                        button = stats_board.inv_buttons['weapon']
                    else:
                        button = stats_board.inv_buttons['armour']
                    if button.selected:
                        button.selected = False
                    else:
                        button.select()

        if mouse_button_state[0]:
            for i in stats_board.buttons.items():
                if i[1].is_over(pos) and not i[1].locked:
                    i[1].selected = True
                if not i[1].is_over(pos):
                    i[1].selected = False
        if not mouse_button_state[0]:
            for i in stats_board.buttons.items():
                if i[1].is_over(pos) and not i[1].locked:
                    i[1].selected = False

        for i in stats_board.buttons.items():
            if i[1].is_over(pos):
                i[1].hovering = True
            elif not (i[1].is_over(pos)) and i[1].hovering:
                i[1].hovering = False
        for i in stats_board.inv_buttons.items():
            if i[1].is_over(pos):
                i[1].hovering = True
            elif not (i[1].is_over(pos)) and i[1].hovering:
                i[1].hovering = False

        if move_limiter != 0:
            if move_limiter == move_limit:
                move_limiter = 0
            else:
                move_limiter += 1

        if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and move_limiter == 0:
            if game_board.game_map[player.y - 1][player.x].can_stand():
                player.move_up(-1)
            move_limiter += 1
        if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and move_limiter == 0:
            if game_board.game_map[player.y + 1][player.x].can_stand():
                player.move_up(1)
            move_limiter += 1
        if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and move_limiter == 0:
            if game_board.game_map[player.y][player.x - 1].can_stand():
                player.move_right(-1)
            move_limiter += 1
        if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and move_limiter == 0:
            if game_board.game_map[player.y][player.x + 1].can_stand():
                player.move_right(1)
            move_limiter += 1

        if type(current_tile) == SecretWallTile:
            if not current_tile.found:
                current_tile.reveal(game_board.game_map)

        if current_tile.is_door():
            current_tile.asset = current_tile.asset_two
            changed_tiles.append(current_tile)

        if current_tile.item is not None:
            if current_tile.item.type == "item" and player.inventory["item"] is None:
                stats_board.buttons["pickup"].locked = False
            else:
                stats_board.buttons["pickup"].locked = True
            if current_tile.item.type == "magic" and player.inventory["magic"] is None:
                stats_board.buttons["pickup"].locked = False
            if current_tile.item.type == "weapon" and player.inventory["weapon"] is None:
                stats_board.buttons["pickup"].locked = False
            if current_tile.item.type == "armour" and player.inventory["armour"] is None:
                stats_board.buttons["pickup"].locked = False
        else:
            stats_board.buttons["pickup"].locked = True
        if current_tile.item is None:
            select = stats_board.get_selected_invbutton()
            if select is not None and select.item is not None:
                stats_board.buttons["drop"].locked = False
            else:
                stats_board.buttons["drop"].locked = True
        else:
            stats_board.buttons["drop"].locked = True

        for i in changed_tiles:
            if i != current_tile and i.is_door():
                i.asset = i.asset_one
                changed_tiles.remove(i)

        draw_window(game_board, stats_board)
    quit()


if __name__ == "__main__":
    main()
