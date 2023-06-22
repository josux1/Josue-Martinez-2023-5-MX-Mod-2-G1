import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, BLAST_SOUND, SCREEN_HEIGHT


class Bullet(Sprite):
    def __init__(self, x, y, is_enemy):
         self.image_width = 10
         self.image_height = 20
         if(is_enemy):
             self.image = BULLET_ENEMY
         else:
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

    def fire_2(self):
        self.rect.y += self.speed
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.available = False