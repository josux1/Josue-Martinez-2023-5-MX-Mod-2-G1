import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_SHIELD, BOOM
from game.components.spaceship.bullet import Bullet

# Sprite = Objeto Dibujable
class Spaceship(Sprite):
    def __init__(self):
        self.image_width = 40
        self.image_height = 70
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.image_height
        self.rect.x = SCREEN_WIDTH // 2 - self.image_width//2
        self.speed = 20
        self.bullets = []

        self.impact_sound = BOOM
        self.impacts = 0

        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.draw_bullets(screen)
        self.set_image(screen, self.rect.x, self.rect.y, SPACESHIP_SHIELD, 50, 70, self.has_shield)
        self.set_image(screen, self.rect.x, self.rect.y, SPACESHIP, 40, 70, not self.has_shield)
    
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
        bullet = Bullet(self.rect.x, self.rect.y, False)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.fire()
            if not bullet.available:
                self.bullets.remove(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)

    def lose(self, enemy_handler):
        for enemy in enemy_handler.enemies:
            for enemy_bullet in enemy_handler.bullets:
                print(self.impacts)
                if(enemy_bullet.rect.colliderect(self.rect) and self.has_shield == False and self.impacts >= 10):
                    self.impacts = 0
                    return True
                if(enemy_bullet.rect.colliderect(self.rect) and self.has_shield):
                    self.has_shield = False
                    self.impact_sound.play()
                    self.impacts += 1
                    return False
                if(enemy_bullet.rect.colliderect(self.rect) and self.has_shield == False):
                    self.impacts += 1
                    return False
    
    def reset(self):
        self.rect.y = SCREEN_HEIGHT - self.image_height
        self.rect.x = SCREEN_WIDTH // 2 - self.image_width//2
        self.bullets = []
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.image_height
        self.rect.x = SCREEN_WIDTH // 2 - self.image_width//2

    def set_image(self, screen, x, y, image, width, height, condition):
        if(condition):
            self.image_width = width
            self.image_height = height
            self.image = image
            self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
            self.rect = self.image.get_rect()
            self.rect.y = y
            self.rect.x = x 
            screen.blit(self.image, (self.rect.x, self.rect.y))
            return

    def verify_shield(self, shields):
        for shield in  shields:
            if(shield.rect.colliderect(self.rect) and not self.has_shield):
                shield.is_alive = False
                self.has_shield = True
                self.impacts = 0
                shield.sound.play()
            elif(shield.rect.colliderect(self.rect) and self.has_shield):
                return
                
    

        
