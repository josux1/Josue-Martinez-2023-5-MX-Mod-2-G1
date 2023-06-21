import pygame
import random
from game.utils.constants import ENEMY_1, ENEMY_2
from game.components.enemies.enemy import Enemy

class EnemyShip(Enemy):
    WIDTH = 40
    HEIGHT = 60
    IMAGES = [ENEMY_1, ENEMY_2]

    def __init__(self):
        self.image = random.choice(self.IMAGES)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)