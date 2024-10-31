import pygame
from settings import *
from os.path import join

class Score:
    def __init__(self, player, ai):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface(SCORE_SIZE)
        self.rect = self.surface.get_rect(topleft = (0, 0))
        self.player = player
        self.ai = ai
        self.playerApple = player.apple
        self.aiApple = ai.apple
        self.font = pygame.font.Font(join('', 'font', 'Russo_One.ttf'), 30)

    def display(self, row, col, player, apple):
        surface = self.font.render(f'{player} : {apple}', True, 'blue')
        rect = surface.get_rect(topleft = (col, row))
        self.surface.blit(surface, rect)
    def update(self):
        self.playerApple = self.player.apple
        self.aiApple = self.ai.apple
    def run(self):        
        self.update()
        self.display_surface.blit(self.surface, (2 * PADDING + GAME_SIZE.x, PADDING))
        self.surface.fill(BACKGROUND_GAME_COLOR)
        pygame.draw.rect(self.surface, LINE_COLOR, self.rect, 2, 2)
        self.display(50, PADDING, "player", self.playerApple)
        self.display(self.surface.get_height() - 50, PADDING, "computer", self.aiApple)