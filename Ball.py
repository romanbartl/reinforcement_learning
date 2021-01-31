import pygame 
import numpy as np
from Player import Player


DEFAULT_DIAMETER = 16
DEFAULT_COLOR = (0, 128, 0)
# DEFAULT_STEP = 0.5


class Ball(object):
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.diameter = DEFAULT_DIAMETER
        
        x = (self.screen_size[0] - self.diameter) / 2
        y = self.screen_size[1] - self.diameter - 40
        
        self.position = np.array([x, y])
        self.speed = 1

        self.direction = np.array([0.5, -0.25])
        self.velocity = self.direction * self.speed


    def draw(self, screen):
        pygame.draw.circle(screen, DEFAULT_COLOR, (self.position[0], self.position[1]), self.diameter)


    def update(self, objects):
        bottom_collision = self.check_collisions(objects)
        self.position = np.add(self.position, self.velocity)
        return bottom_collision


    def change_x_direction(self):
        self.velocity = np.multiply(self.velocity, np.array([-1, 1]))


    def change_y_direction(self):
        self.velocity = np.multiply(self.velocity, np.array([1, -1]))


    def check_border_collisons(self):
        # TODO ball almost never touches a wall
        collision_bottom = self.position[1] + self.diameter > self.screen_size[1]

        if collision_bottom:
            return True

        collision_left = self.position[0] < self.diameter
        collision_right = self.position[0] + self.diameter > self.screen_size[0]
        collision_top = self.position[1] < self.diameter

        if collision_left or collision_right:
            self.change_x_direction()

        if collision_top:
            self.change_y_direction()

        return False


    def clamp(self, min, max, value):
        if value < min:
            return min
        elif value > max:
            return max
        return value


    def check_object_collision(self, obj):
        obj_x = obj.get_x()
        obj_y = obj.get_y()
        obj_w = obj.get_width()
        obj_h = obj.get_height()

        x_point = self.clamp(obj_x, obj_x + obj_w, self.position[0])
        y_point = self.clamp(obj_y, obj_y + obj_h, self.position[1])

        distance = (x_point - self.position[0])**2 + (y_point - self.position[1])**2

        if self.diameter**2 > distance:
            return True
        
        return False


    def check_collisions(self, objects):
        if self.check_border_collisons():
            return True

        for obj in objects:
            if self.check_object_collision(obj):
                if type(obj) == Player:
                    self.change_y_direction()

        return False

