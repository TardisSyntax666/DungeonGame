import os
import pygame


class StatsUI:
    def __init__(self, inventory):
        self.asset = pygame.image.load(os.path.join("assets", "ui1.png"))
        self.inventory = inventory
        self.buttons = {'item': ItemInvButton(inventory, (310, 746)), 'magic': MagicInvButton(inventory, (370, 746)),
                        'weapon': WeaponInvButton(inventory, (430, 746)), 'armour': ArmourInvButton(inventory, (490, 746))}

    def render(self, window, pos):
        window.blit(self.asset, pos)
        for i in self.buttons.items():
            i[1].render(window)

    def update_inventory(self, inventory):
        pass


class Button:
    def __init__(self, pos, size):
        self.x = pos[0]
        self.y = pos[1]

        self.width = size[0]
        self.height = size[1]

        self.asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        self.hover_asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        self.selected_asset = pygame.image.load(os.path.join("assets", "no_texture.png"))

        self.hovering = False
        self.selected = False

    def render(self, window):
        pass

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


class InvButton(Button):
    def __init__(self, pos):
        super().__init__(pos, (25, 25))
        self.asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        self.hover_asset = pygame.image.load(os.path.join("assets", "button_hover.png"))
        self.select_asset = pygame.image.load(os.path.join("assets", "button_select.png"))
        self.item = None

    def render(self, window):
        window.blit(self.asset, (self.x, self.y))
        if self.selected and not self.hovering:
            window.blit(self.select_asset, (self.x, self.y))
        if self.hovering:
            window.blit(self.hover_asset, (self.x, self.y))
        if self.item is not None:
            item = pygame.transform.scale(self.item.asset, (50, 50))
            window.blit(item, (self.x, self.y))


class ItemInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "item_button.png"))
        self.inventory = inventory
        self.item = inventory['item']


class MagicInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "magic_button.png"))
        self.inventory = inventory
        self.item = inventory['magic']


class WeaponInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "weapon_button.png"))
        self.inventory = inventory
        self.item = inventory['weapon']


class ArmourInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "armour_button.png"))
        self.inventory = inventory
        self.item = inventory['armour']
