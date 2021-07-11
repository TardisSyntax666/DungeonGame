import os

import pygame


class StatsUI:
    def __init__(self, inventory):
        self.asset = pygame.image.load(os.path.join("assets", "ui1.png"))
        self.inventory = inventory
        self.inv_buttons = {'item': ItemInvButton(inventory, (385, 744)),
                            'magic': MagicInvButton(inventory, (445, 744)),
                            'weapon': WeaponInvButton(inventory, (505, 744)),
                            'armour': ArmourInvButton(inventory, (565, 744))}
        self.buttons = {'pickup': Button((385, 709), (110, 30), "pickup_button.png", "drop&pickup_hover.png",
                                         "pickup_button_select.png", "pickup_button_locked.png"),
                        'drop': Button((505, 709), (110, 30), "drop_button.png", "drop&pickup_hover.png",
                                       "drop_button_select.png", "drop_button_locked.png")}
        for i in self.inv_buttons.items():
            for e in self.inv_buttons.items():
                if not (i == e):
                    i[1].family.append(e[1])

        for button in self.buttons.items():
            button[1].locked = True

    def render(self, window, pos):
        window.blit(self.asset, pos)
        for i in self.buttons.items():
            i[1].render(window)
        for i in self.inv_buttons.items():
            i[1].render(window)

    def update_inventory(self, inventory):
        self.inventory = inventory
        for button in self.inv_buttons.items():
            button[1].update_item(inventory)

    def get_selected_invbutton(self):
        num = 0
        for button in self.inv_buttons.items():
            num += 1
            if button[1].selected:
                return button[1]
        if num == len(self.inv_buttons.items()):
            return None


class Button:
    def __init__(self, pos, size, asset1=None, asset2=None, asset3=None, asset4=None):
        self.x = pos[0]
        self.y = pos[1]

        self.width = size[0]
        self.height = size[1]

        if asset1 is None:
            self.asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        else:
            self.asset = pygame.image.load(os.path.join("assets", asset1))
        if asset2 is None:
            self.hover_asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        else:
            self.hover_asset = pygame.image.load(os.path.join("assets", asset2))
        if asset3 is None:
            self.selected_asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        else:
            self.selected_asset = pygame.image.load(os.path.join("assets", asset3))
        if asset4 is not None:
            self.locked_asset = pygame.image.load(os.path.join("assets", asset4))

        self.hovering = False
        self.selected = False
        self.locked = False

    def render(self, window):
        if self.locked:
            window.blit(self.locked_asset, (self.x, self.y))
        else:
            if self.selected:
                window.blit(self.selected_asset, (self.x, self.y))
            else:
                window.blit(self.asset, (self.x, self.y))
            if self.hovering:
                window.blit(self.hover_asset, (self.x, self.y))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


class InvButton(Button):
    def __init__(self, pos):
        super().__init__(pos, (50, 50))
        self.asset = pygame.image.load(os.path.join("assets", "no_texture.png"))
        self.hover_asset = pygame.image.load(os.path.join("assets", "button_hover.png"))
        self.select_asset = pygame.image.load(os.path.join("assets", "button_select.png"))
        self.item = None
        self.family = []

    def select(self):
        self.selected = True
        for i in self.family:
            i.selected = False

    def render(self, window):
        window.blit(self.asset, (self.x, self.y))
        if self.selected:
            window.blit(self.select_asset, (self.x, self.y))
        if self.hovering:
            window.blit(self.hover_asset, (self.x, self.y))
        if self.item is not None:
            item = pygame.transform.scale(self.item.asset, (38, 38))
            window.blit(item, (self.x + 6, self.y + 6))


class ItemInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "item_button.png"))
        self.item = inventory['item']

    def update_item(self, inventory):
        self.item = inventory['item']


class MagicInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "magic_button.png"))
        self.item = inventory['magic']

    def update_item(self, inventory):
        self.item = inventory['magic']


class WeaponInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "weapon_button.png"))
        self.item = inventory['weapon']

    def update_item(self, inventory):
        self.item = inventory['weapon']


class ArmourInvButton(InvButton):
    def __init__(self, inventory, pos):
        super().__init__(pos)
        self.asset = pygame.image.load(os.path.join("assets", "armour_button.png"))
        self.item = inventory['armour']

    def update_item(self, inventory):
        self.item = inventory['armour']
