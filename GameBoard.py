import pygame


class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.backgroundColor = (128, 128, 128)
        self.icon = pygame.image.load("img/particle.png")
        self.screen = pygame.display.set_mode((width, height))

        # title and icon
        pygame.display.set_caption("Simulation")
        pygame.display.set_icon(self.icon)

    def draw(self, conduct):
        self.screen.fill(self.backgroundColor)

        conduct.draw_box(self.screen)
        pygame.display.update()
