import pygame

class Block:
    DEFAULT_COLOR = (128, 0, 0)

    def __init__(self, x, y, width, height, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if color is not None:
            self.color = color
        else:
            self.color = self.DEFAULT_COLOR


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    
    def get_x(self):
        return self.x


    def get_y(self):
        return self.y

    
    def get_width(self):
        return self.width


    def get_height(self):
        return self.height
