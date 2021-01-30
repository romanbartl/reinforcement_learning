import pygame 

DEFAULT_DIAMETER = 16
DEFAULT_COLOR = (0, 128, 0)
DEFAULT_STEP = 0.5

class Ball(object):
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.diameter = DEFAULT_DIAMETER
        self.x = (self.screen_size[0] - self.diameter) / 2
        self.y = self.screen_size[1] - self.diameter - 40
        self.step = DEFAULT_STEP

    def draw(self, screen):
        if self.y != 0:
            self.y = self.y - self.step
        pygame.draw.circle(screen, DEFAULT_COLOR, (self.x, self.y), self.diameter)