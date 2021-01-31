import pygame 
import math

DEFAULT_HEIGHT = 20
DEFAULT_WIDTH = 200

DEFAULT_COLOR = (0, 0, 128)

class Player(object):
    def __init__(self, screen_size):
        self.screen_size = screen_size

        x = (self.screen_size[0] - DEFAULT_WIDTH) / 2
        y = self.screen_size[1] - DEFAULT_HEIGHT - 20

        self.rect = pygame.rect.Rect((x, y, DEFAULT_WIDTH, DEFAULT_HEIGHT))


    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        
        if key[pygame.K_LEFT]:
            if self.rect.x != 0:
                self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
            if self.rect.x != self.screen_size[0] - self.rect.width:
                self.rect.move_ip(1, 0)


    def draw(self, screen):
        pygame.draw.rect(screen, DEFAULT_COLOR, self.rect)


    def set_width(self, width):
        self.rect.width = width


    def set_height(self, height):
        self.rect.height = height

 
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y


    def get_x(self):
        return self.rect.x


    def get_y(self):
        return self.rect.y

    
    def get_width(self):
        return self.rect.width


    def get_height(self):
        return self.rect.height

