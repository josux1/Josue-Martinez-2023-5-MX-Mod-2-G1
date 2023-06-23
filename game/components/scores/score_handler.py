import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class ScoreHandler:
    def __init__(self):
        self.highest_score = 0
        self.current_score = 0
        self.total_deaths = 0
        self.timer = 0
        self.loose = False

    def draw_scores(self, screen):
        self.set_score('Total Deaths:', 38, self.total_deaths, screen, 10, 10)
        self.set_score('Score:', 38, self.current_score, screen, 60, 10)

    def draw_game_over_screen(self, screen):
        self.loose = True
        game_over_surface = pygame.Surface(screen.get_size())
        game_over_surface.fill((0, 0, 0))
        game_over_surface.set_alpha(128)
        screen.blit(game_over_surface, (0, 0))
        self.set_text('Game Over', 80, screen, SCREEN_HEIGHT / 4 )
        self.set_text('Press R to restart', 30, screen, SCREEN_HEIGHT / 3)
        self.set_score('Your Score:', 40, self.current_score, screen, SCREEN_HEIGHT * 0.6)
        self.set_score('Highest Score:', 40, self.highest_score, screen, SCREEN_HEIGHT * 0.7)
        self.set_score('Total Deaths:', 40, self.total_deaths, screen, SCREEN_HEIGHT * 0.8)

    def continue_game(self, keyboard_events):
        if(self.current_score > self.highest_score):
            self.highest_score = self.current_score
            
        if (keyboard_events[pygame.K_r] and self.loose):
            self.current_score = 0
            self.total_deaths = 0
            self.timer = 0
            self.loose = False
            return True
        
    def set_text(self, text, font_size, screen, y):
        font = pygame.font.Font(None, font_size)
        score_text = font.render(text, True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2 , y))

    def set_score(self, text, font_size, number, screen, y, x=0):
        if(x == 0):
            font = pygame.font.Font(None, font_size)
            score_text = font.render(f'{text} {number}', True, (255, 255, 255))
            x = SCREEN_WIDTH / 2 - score_text.get_width() / 2 
            screen.blit(score_text, (x, y))
        else:
            font = pygame.font.Font(None, font_size)
            score_text = font.render(f'{text} {number}', True, (255, 255, 255))
            screen.blit(score_text, (x , y))

