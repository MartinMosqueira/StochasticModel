import pygame

class Conduct:
    def __init__(self):
        self.width = 200
        self.height = 300
        self.radius = 200
        self.color = (80, 80, 80)

    def draw_box(self, screen):
        x = (screen.get_width() - self.width) // 2
        y = (screen.get_height() - self.height) // 2
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))

    def draw_circle(self, screen):
        x = screen.get_width() // 2
        y = screen.get_height() // 2
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
    
    def get_collision_box(self, particle, screenWidth, screenHeight):
        x, y = particle.get_position()
        
        # Calculating box coordinates
        box_x_min = (screenWidth - self.width) // 2
        box_x_max = box_x_min + self.width
        box_y_min = (screenHeight - self.height) // 2
        box_y_max = box_y_min + self.height
        
        # Check collision with the box
        if box_x_min < x < box_x_max and box_y_min < y < box_y_max:
            return False    
        return True
    
    def get_collision_circle(self, particle, screenWidth, screenHeight):
        x, y = particle.get_position()
        
        # Calculating circle center
        circle_center_x = screenWidth // 2
        circle_center_y = screenHeight // 2

        # Check collision with the circle
        distance = ((x - circle_center_x) ** 2 + (y - circle_center_y) ** 2) ** 0.5
        if distance < self.radius:
            return False
        return True