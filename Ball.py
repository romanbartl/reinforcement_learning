import pygame 

DEFAULT_DIAMETER = 16
DEFAULT_COLOR = (0, 128, 0)
DEFAULT_STEP = 0.5

class Ball(object):
    def __init__(self, mw, screen_size):
        self.mw = mw
        self.screen_size = screen_size
        self.diameter = DEFAULT_DIAMETER
        self.x = (self.screen_size[0] - self.diameter) / 2
        self.y = self.screen_size[1] - self.diameter - 40
        self.step = DEFAULT_STEP
        self.direction = -1

    def draw(self, screen):
        # collision with top border
        if self.y == self.diameter:
            self.change_direction()
        # collision with bottom border
        if self.y == self.screen_size[1] - self.diameter:
            self.game_over()

        self.y = self.y + self.direction * self.step
        pygame.draw.circle(screen, DEFAULT_COLOR, (self.x, self.y), self.diameter)

    def change_direction(self):
        self.direction = self.direction * -1

    def game_over(self):
        self.mw.game_over()
