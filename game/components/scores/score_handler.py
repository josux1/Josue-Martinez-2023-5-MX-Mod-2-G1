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
        font = pygame.font.Font(None, 38)
        score_text = font.render(f'Total Deaths: {self.total_deaths}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        font2 = pygame.font.Font(None, 38)
        score_text2 = font2.render(f'Score: {self.current_score}', True, (255, 255, 255))
        screen.blit(score_text2, (SCREEN_WIDTH - score_text2.get_width() - 15, 10))

    def draw_game_over_screen(self, screen):
        self.loose = True
        game_over_surface = pygame.Surface(screen.get_size())
        game_over_surface.fill((0, 0, 0))
        game_over_surface.set_alpha(128)
        screen.blit(game_over_surface, (0, 0))

        font = pygame.font.Font(None, 80)
        score_text = font.render('Game Over', True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2 , SCREEN_HEIGHT / 4))
        font5 = pygame.font.Font(None, 30)
        score_text5 = font5.render('Press R to restart', True, (255, 255, 255))
        screen.blit(score_text5, (SCREEN_WIDTH / 2 - score_text5.get_width() / 2 , SCREEN_HEIGHT / 3))

        font2 = pygame.font.Font(None, 40)
        score_text2 = font2.render(f'Your Score: {self.current_score}', True, (255, 255, 255))
        screen.blit(score_text2, (SCREEN_WIDTH / 2 - score_text2.get_width() / 2 , SCREEN_HEIGHT * 0.6))
        font3 = pygame.font.Font(None, 40)
        score_text3 = font3.render(f'Highest Score: {self.highest_score}', True, (255, 255, 255))
        screen.blit(score_text3, (SCREEN_WIDTH / 2 - score_text3.get_width() / 2 , SCREEN_HEIGHT * 0.7))
        font4 = pygame.font.Font(None, 40)
        score_text4 = font4.render(f'Total Deaths: {self.total_deaths}', True, (255, 255, 255))
        screen.blit(score_text4, (SCREEN_WIDTH / 2 - score_text4.get_width() / 2 , SCREEN_HEIGHT * 0.8))

    def continue_game(self, keyboard_events):
        if(self.current_score > self.highest_score):
            self.highest_score = self.current_score
            
        if (keyboard_events[pygame.K_r] and self.loose):
            self.current_score = 0
            self.total_deaths = 0
            self.timer = 0
            self.loose = False
            return True

