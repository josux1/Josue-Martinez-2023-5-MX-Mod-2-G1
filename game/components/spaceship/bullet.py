import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BLAST_SOUND


class Bullet(Sprite):
    def __init__(self, x, y):
         self.image_width = 10
         self.image_height = 20
         self.image = BULLET
         self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.speed = 10
         self.available = True
         self.sound = BLAST_SOUND

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def fire(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.available = False