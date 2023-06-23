import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, SHIELD, SHIELD_SOUND

class Shield(Sprite):    
    X_POS_LIST = [100, 150, 200, 250, 300, 350, 400, 450]

    def __init__(self):
        self.image_width = 20
        self.image_height = 50
        self.image = SHIELD
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.choice(self.X_POS_LIST)
        self.speed = 5
        self.is_alive = True
        self.sound = SHIELD_SOUND

    def update(self):
        if(self.rect.y >= SCREEN_HEIGHT):
            self.is_alive = False
        self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.speed