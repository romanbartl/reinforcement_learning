import pygame
from GameState import GameState
from Player import Player
from Ball import Ball
from Block import Block
from Actions import Actions
import random


class Environment:
    DEFAULT_WIDTH = 1024
    DEFAULT_HEIGHT = 768
    DEFAULT_BACKGROUND_COLOR = (255, 255, 255)
    DEFAULT_PADDING = 10
    DEFAULT_BLOCKS_START_HEIGHT = 300
    DEFAULT_ROWS = 3
    DEFAULT_BLOCK_HEIGHT = 20


    def __init__(self, human_play=True):
        self.human_play = human_play

        self.screen_w = self.DEFAULT_WIDTH
        self.screen_h = self.DEFAULT_HEIGHT
        self.background_color = self.DEFAULT_BACKGROUND_COLOR

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.screen_w, self.screen_h])

        self.reset_game()


    def generate_new_block(self, x, y, width, heigth):
        self.objects.append(Block(x, y, width, heigth))


    def generate_blocks(self):
        max_width = int(self.screen_w / 10)
        min_width = int(max_width / 2)

        start_x = 0
        start_y = self.DEFAULT_BLOCKS_START_HEIGHT
        new_width = 0
        row = 0

        while True:
            start_x += new_width + self.DEFAULT_PADDING

            if start_x + max_width + self.DEFAULT_PADDING > self.screen_w:
                new_width = self.screen_w - self.DEFAULT_PADDING - start_x
                self.generate_new_block(start_x, start_y, new_width, self.DEFAULT_BLOCK_HEIGHT)

                row += 1

                if row == self.DEFAULT_ROWS:
                    break

                start_x = self.DEFAULT_PADDING
                start_y -= self.DEFAULT_BLOCK_HEIGHT + self.DEFAULT_PADDING
            else:
                new_width = random.randint(min_width, max_width)

            self.generate_new_block(start_x, start_y, new_width, self.DEFAULT_BLOCK_HEIGHT)


    def reset_game(self):
        self.ball = Ball([self.screen_w, self.screen_h])
        self.player = Player([self.screen_w, self.screen_h])
        self.objects = [self.player]

        self.generate_blocks()

        self.reward = 0

        self.game_state = GameState.RUNNING


    def catch_event(self):
        action = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.QUIT

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            action = Actions.LEFT
        if key[pygame.K_RIGHT]:
            action = Actions.RIGHT

        return action


    def game_over(self):
        self.game_state = GameState.GAME_OVER


    def step(self, action):
        self.reward = 0

        if action == Actions.LEFT:
            self.player.move_left()
        elif action == Actions.RIGHT:
            self.player.move_right()
        else:
            self.player.stop()
    
        bottom_border_colision, colided_block = self.ball.update(self.objects)

        if bottom_border_colision:
            # TODO reward down
            self.game_over()

        if colided_block is not None:
            del self.objects[colided_block]

        # return game_state, reward, objects states
        return self.game_state, self.reward, [self.objects, self.ball]


    def render_scene(self):
        if self.human_play:
            action = self.catch_event()
            self.step(action)

        self.screen.fill(self.background_color)
        self.ball.draw(self.screen)

        for obj in self.objects:
            obj.draw(self.screen)

        pygame.display.update()
        self.clock.tick(1000)


    def get_game_state(self):
        return self.game_state
    

    def pygame_quit(self):
        pygame.quit()
