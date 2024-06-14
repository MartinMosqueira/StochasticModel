import pygame
from pygame.locals import *
import sys
from GameBoard import GameBoard
from Conduct import Conduct

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

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                
            # draw board
            self.board.draw(self.conduct)

            self.clock.tick(15)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()