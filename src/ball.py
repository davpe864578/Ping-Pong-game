import random

import pygame

from src.configs import *


class Ball:
    def __init__(self, screen, clock, pos_x, pos_y, radius, speed, color):
        self.screen = screen
        self.clock = clock
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.speed_x = speed * random.choice([1, -1])
        self.speed_y = speed * random.choice([1, -1])
        self.color = color

        self.rect = pygame.Rect(pos_x - radius, pos_y - radius, radius * 2, radius * 2)

    def update(self, player1_rect, player2_rect):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.rect.center = (self.pos_x, self.pos_y)

        if self.pos_y - self.radius < 0 or self.pos_y + self.radius > SCREEN_HEIGHT:
            self.speed_y *= -1

        if self.rect.colliderect(player1_rect) or self.rect.colliderect(player2_rect):
            self.speed_x *= -1

        if self.pos_x - self.radius < 0 or self.pos_x + self.radius > SCREEN_WIDTH:
            return True

        return False


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.pos_x, self.pos_y), self.radius)
