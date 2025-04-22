import pygame

from src.configs import *


class Player:
    def __init__(self, screen, clock, pos_x, pos_y, width, height, speed, color, key_down, key_up):
        self.screen = screen
        self.clock = clock
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.key_down = key_down
        self.key_up = key_up

        self.rect = pygame.Rect(pos_x, pos_y, width, height)

    def update(self, keys_pressed):
        if keys_pressed[self.key_down]:
            self.pos_y += self.speed
            self.rect.y += self.speed
        if keys_pressed[self.key_up]:
            self.pos_y -= self.speed
            self.rect.y -= self.speed

        if self.pos_y < 0:
            self.pos_y = 0
            self.rect.y = 0
        elif self.pos_y + self.height > SCREEN_HEIGHT:
            self.pos_y = SCREEN_HEIGHT - self.height
            self.rect.y = SCREEN_HEIGHT - self.height

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.pos_x, self.pos_y, self.width, self.height))

    def send_pos_x(self):
        return self.pos_x

    def send_pos_y(self):
        return self.pos_y
        
