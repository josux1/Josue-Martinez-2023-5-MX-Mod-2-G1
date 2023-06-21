import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

from game.components.spaceship.bullet import Bullet

# Sprite = Objeto Dibujable
class Spaceship(Sprite):
    def __init__(self):
        self.image_width = 40
        self.image_height = 70
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.image_height
        self.rect.x = SCREEN_WIDTH // 2 - self.image_width//2
        self.speed = 20
        self.bullets = []
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.draw_bullets(screen)
    
    def update(self, keyboard_events):
        if (keyboard_events[pygame.K_LEFT] and self.rect.x >= 0):
            self.move_left()
        if (keyboard_events[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.image_width):
            self.move_right()
        if (keyboard_events[pygame.K_UP] and self.rect.y >= 0):
            self.move_up()
        if (keyboard_events[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.image_height):
            self.move_down()
        if (keyboard_events[pygame.K_SPACE]):
            self.fire()
        self.update_bullets()

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def fire(self):
        bullet = Bullet(self.rect.x, self.rect.y)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.fire()
            if not bullet.available:
                self.bullets.remove(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)

        
