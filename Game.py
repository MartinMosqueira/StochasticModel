import pygame
from pygame.locals import *
import sys
from GameBoard import GameBoard
from Conduct import Conduct
from Particle import Particle
import random


class Game:
    def __init__(self):
        # initialize the game engine
        pygame.init()

        self.x = 700
        self.y = 700

        # sets the initial map
        self.board = GameBoard(self.x, self.y)
        
        # sets the initial conduct
        self.conduct = Conduct()

        # list of particles
        self.particles = []
        self.particlesColided = []

        self.clock = pygame.time.Clock()
        self.running = True
    
    def init_particles(self):
        # initial position of the particle
        self.px = self.board.width // 2
        self.py = self.board.height // 2

        self.particles.append(Particle(5, self.px, self.py))

    def run(self):
        self.init_particles()

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                
            # draw board
            self.board.draw(self.conduct)

            # draw particle
            for particle in self.particles:
                particle.draw(self.board.screen)
            
            # draw particles colided
            for particle in self.particlesColided:
                particle.draw(self.board.screen)

            pygame.display.update()

            # check collision
            for particle in self.particles:
                if self.conduct.get_collision_box(particle, self.x, self.y):
                    self.particlesColided.append(particle)
                    self.particles.remove(particle)
                    self.init_particles()
                
                elif particle.get_colision_particle(self.particlesColided):
                    self.particlesColided.append(particle)
                    self.particles.remove(particle)
                    self.init_particles()

                else:
                    particle.x += random.randint(-10, 10)
                    particle.y += random.randint(-10, 10)

            self.clock.tick(20)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()