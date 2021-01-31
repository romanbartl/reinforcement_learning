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

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.player.move_left()
        if key[pygame.K_RIGHT]:
            self.player.move_right()


    def get_screen_size(self):
        return WIN_WIDTH, WIN_HEIGHT


    def game_over(self):
        self.state = GameState.GAME_OVER


    def run(self):
        self.state = GameState.RUNNING
        
        self.player = Player((WIN_WIDTH, WIN_HEIGHT))
        self.objects.append(self.player)
        self.ball = Ball([WIN_WIDTH, WIN_HEIGHT])

        while self.state == GameState.RUNNING:
            self.catch_event()

            self.screen.fill(WHITE_BACKGROUND)

            self.player.draw(self.screen)

            bottom_border_colision = self.ball.update(self.objects)

            if bottom_border_colision:
                self.game_over()
                break

            self.ball.draw(self.screen)

            pygame.display.update()
            self.clock.tick(1000)

        if self.state == GameState.GAME_OVER:
            print("game over")

        pygame.quit()
