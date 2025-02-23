import pygame
import time

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, GAME_OVER_SOUND
from game.components.spaceship.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.scores.score_handler import ScoreHandler
from game.components.powers.shield_handler import ShieldHandler


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.score_handler = ScoreHandler()
        self.game_over = False

        self.shield_handler = ShieldHandler()
        self.game_over_sound = GAME_OVER_SOUND

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something ocurred to quit the game!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # pygame.event.get() es un iterable (lista)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False

    def update(self):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        self.enemy_handler.update()
        self.shield_handler.update()
        self.enemy_handler.verify_explotion(self.spaceship.bullets)
        self.enemy_handler.fire_automaticly()
        self.score_handler.total_deaths = self.enemy_handler.get_deaths()
        self.score_handler.current_score = self.enemy_handler.get_score()
        self.spaceship.verify_shield(self.shield_handler.shields)
        
        if(self.spaceship.lose(self.enemy_handler) and self.game_over == False):
            self.game_over = True
            self.enemy_handler.sound.play()
            self.game_over_sound.play()
        if(self.score_handler.continue_game(events)):
            self.game_over = False
            self.enemy_handler.reset()
            self.spaceship.reset()

            

    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        self.draw_background()

        if(self.game_over):
            self.score_handler.draw_game_over_screen(self.screen)
        else:
            self.spaceship.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.score_handler.draw_scores(self.screen)
            self.shield_handler.draw(self.screen)


        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
