import pygame
from GameState import GameState
from Player import Player
from Ball import Ball


WIN_WIDTH = 1024
WIN_HEIGHT = 768

WHITE_BACKGROUND = (255, 255, 255)


class MainWindow:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        self.objects = []


    def catch_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = GameState.QUIT


    def get_screen_size(self):
        return WIN_WIDTH, WIN_HEIGHT


    def game_over(self):
        self.state = GameState.GAME_OVER


    def ball_collision(self):
        ball_params = self.ball.get_params()

        # collision with top border
        if ball_params['y'] == ball_params['d']:
            self.ball.change_direction()
        # collision with bottom border
        if ball_params['y'] == WIN_HEIGHT - ball_params['d']:
            self.game_over()

        # collision with other objects
        for obj in self.objects:
            if obj.is_colision_with_ball(ball_params):
                self.ball.change_direction()


    def run(self):
        self.state = GameState.RUNNING
        
        self.player = Player((WIN_WIDTH, WIN_HEIGHT))
        self.objects.append(self.player)
        self.ball = Ball([WIN_WIDTH, WIN_HEIGHT])

        while self.state == GameState.RUNNING:
            self.catch_event()

            self.screen.fill(WHITE_BACKGROUND)

            self.player.draw(self.screen)
            self.player.handle_keys()

            self.ball.draw(self.screen)
            self.ball_collision()

            pygame.display.update()
            #pygame.display.flip()
            #self.clock.tick(100)

        if self.state == GameState.GAME_OVER:
            print("game over")

        pygame.quit()
