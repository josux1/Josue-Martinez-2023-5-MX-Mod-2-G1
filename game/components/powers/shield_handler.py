import pygame
from game.components.powers.shield import Shield
from game.utils.constants import BOOM

class ShieldHandler:
    MAX_SHIELDS = 2

    def __init__(self):
        self.shields = []

    def update(self):
        self.add_shield()
        for shield in self.shields:
            shield.update()
            if not shield.is_alive:
                self.remove_shield(shield)

    def draw(self, screen):
        for shield in self.shields:
            shield.draw(screen)

    def add_shield(self):
        if( len(self.shields) < self.MAX_SHIELDS):
            self.shields.append(Shield())

    def remove_shield(self, shield):
        self.shields.remove(shield)