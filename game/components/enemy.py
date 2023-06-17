import pygame
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    def __init__(self):
        self.image_width = 40
        self.image_height = 70
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.image_width//2
        # self.rect.y = SCREEN_HEIGHT
        self.speed = 20

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))