import pygame 

class Player:
    DEFAULT_HEIGHT = 20
    DEFAULT_WIDTH = 200

    DEFAULT_COLOR = (0, 0, 128)

    def __init__(self, screen_size, color=None):
        self.screen_size = screen_size

        self.width = self.DEFAULT_WIDTH
        self.height = self.DEFAULT_HEIGHT
        self.x = (self.screen_size[0] - self.width) / 2
        self.y = self.screen_size[1] - self.height - 20

        if color is None:
            self.color = self.DEFAULT_COLOR
        else:
            self.color = color
            

    def move_left(self):
        if self.x != 0:
            self.x -= 1


    def move_right(self):
        if self.x != self.screen_size[0] - self.width:
            self.x += 1


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


    def set_width(self, width):
        self.width = width


    def set_height(self, height):
        self.height = height

 
    def set_position(self, x, y):
        self.x = x
        self.y = y


    def get_x(self):
        return self.x


    def get_y(self):
        return self.y

    
    def get_width(self):
        return self.width


    def get_height(self):
        return self.height

