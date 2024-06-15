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

        # initial position of the particle
        self.px = self.board.width // 2
        self.py = self.board.height // 2

        self.particle = Particle(3, self.px, self.py)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                
            # draw board
            self.board.draw(self.conduct)

            # draw particle
            self.particle.draw(self.board.screen)

            pygame.display.update()

            if self.conduct.get_collision_box(self.particle, self.x, self.y):
                print("Collision detected")
                self.running = False
            else:
                self.particle.x += random.randint(-10, 10)
                self.particle.y += random.randint(-10, 10)

            self.clock.tick(10)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()