import pygame

class Conduct:
    def __init__(self):
        self.width = 400
        self.height = 500
        self.radius = 300
        self.color = (80, 80, 80)

    def draw_box(self, screen):
        x = (screen.get_width() - self.width) // 2
        y = (screen.get_height() - self.height) // 2
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))

    def draw_circle(self, screen):
        x = screen.get_width() // 2
        y = screen.get_height() // 2
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
