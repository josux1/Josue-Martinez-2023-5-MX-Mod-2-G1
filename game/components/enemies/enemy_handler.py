from game.components.enemies.enemy_ship import EnemyShip
from game.components.spaceship.bullet import Bullet
import pygame

class EnemyHandler:
    MAX_ENEMIES = 5
    DELAY = 1500
    TIMER = 0

    def __init__(self):
        self.enemies = []
        self.bullets = []
        self.deaths = 0
        self.score = 0
        self.score_amount = 7

    def update(self):
        self.add_enemy()
        self.update_bullets()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        self.draw_bullets(screen)
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if( len(self.enemies) < self.MAX_ENEMIES):
            self.enemies.append(EnemyShip())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def verify_explotion(self, bullets):
        for enemy in self.enemies:
            for bullet in bullets:
                if enemy.rect.colliderect(bullet.rect):
                    self.deaths += 1
                    self.score += self.score_amount
                    enemy.is_alive = False
                    bullet.sound.play()
    
    def fire_automaticly(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.TIMER >= self.DELAY:
            for enemy in self.enemies:
                self.fire(enemy.rect.x, enemy.rect.y)
                self.TIMER = current_time

    def fire(self, x, y):
        bullet = Bullet(x, y, True)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.fire_2()
            if not bullet.available:
                self.bullets.remove(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)

    def get_deaths(self):
        return self.deaths
    
    def get_score(self):
        return self.score
    
    def reset_score(self):
        self.deaths = 0
        self.score = 0
