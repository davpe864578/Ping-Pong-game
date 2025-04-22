import pygame

from src.configs import *
from src.game import Game


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping-Pong")
    clock = pygame.time.Clock()

    game = Game(screen, clock)
    
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        keys_pressed = pygame.key.get_pressed()
        fl_end_game = game.update(keys_pressed)
        game.draw()

        game_running = not fl_end_game

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

