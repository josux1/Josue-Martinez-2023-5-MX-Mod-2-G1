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
        self.speed = 5
        self.flying = True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_automaticly_y(self):
        if(self.rect.y == SCREEN_HEIGHT - self.image_height * 2):
            self.flying = False
        if(self.rect.y == 0):
            self.flying = True

        if self.flying and self.rect.y != SCREEN_HEIGHT - self.image_height * 2 :
            self.move_down()
        else:
            self.move_up()
            

    def move_down(self):
        self.rect.y += self.speed

    def move_up(self):
        self.rect.y -= self.speed
