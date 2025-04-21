import pygame

from src.configs import *
from src.player import Player

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        
        self.background = BLACK

        self.player1 = Player(self.screen, self.clock, 20, 20, 12, 75, 5, WHITE, pygame.K_DOWN, pygame.K_UP)
        self.player2 = Player(self.screen, self.clock, 868, 20, 12, 75, 5, WHITE, pygame.K_s, pygame.K_w)

    def update(self, keys_pressed): 
        self.screen.fill(self.background)
        self.player1.update(keys_pressed)
        self.player2.update(keys_pressed)

    def draw(self): 
        self.player1.draw()
        self.player2.draw()
