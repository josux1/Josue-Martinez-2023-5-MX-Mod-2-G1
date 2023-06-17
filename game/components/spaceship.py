import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Sprite = Objeto Dibujable
class Spaceship(Sprite):
    def __init__(self):
        self.image_width = 40
        self.image_height = 70
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.image_height
        self.rect.x = SCREEN_WIDTH // 2
        self.speed = 20
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self, keyboard_events):
        if (keyboard_events[pygame.K_LEFT] and self.rect.x >= 0):
            self.move_left()
        if (keyboard_events[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.image_width):
            self.move_right()

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed
        
