import pygame


class Particle:
    def __init__(self, size, x, y):
        # size particle in mm
        self.size=size
        # position of particle
        self.x = x
        self.y = y
        # color of particle
        self.color = (135, 206, 235)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def get_position(self):
        return self.x, self.y
        