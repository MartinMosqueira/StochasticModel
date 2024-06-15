import pygame
import math


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
    
    def get_colision_particle(self, particlesColided):
        for p in particlesColided:
            if self._check_collision(p):
                return True
        return False

    def _check_collision(self, other):
        # Calculate distance between particles
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance < (self.size + other.size)