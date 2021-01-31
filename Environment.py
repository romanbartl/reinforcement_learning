import pygame
from GameState import GameState
from Player import Player
from Ball import Ball
from Actions import Actions


class Environment:
    DEFAULT_WIDTH = 1024
    DEFAULT_HEIGHT = 768
    DEFAULT_BACKGROUND_COLOR = (255, 255, 255)


    def __init__(self, human_play=True):
        self.human_play = human_play

        self.screen_w = self.DEFAULT_WIDTH
        self.screen_h = self.DEFAULT_HEIGHT
        self.background_color = self.DEFAULT_BACKGROUND_COLOR

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.screen_w, self.screen_h])

        self.reset_game()


    def reset_game(self):
        self.ball = Ball([self.screen_w, self.screen_h])
        self.player = Player([self.screen_w, self.screen_h])
        self.objects = [self.player]

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
        
        if action == Actions.RIGHT:
            self.player.move_right()
    
        bottom_border_colision = self.ball.update(self.objects)

        if bottom_border_colision:
            # TODO reward down
            self.game_over()

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
    