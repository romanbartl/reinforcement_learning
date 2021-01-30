import pygame
from GameState import GameState
from Player import Player


WIN_WIDTH = 1024
WIN_HEIGHT = 768

WHITE_BACKGROUND = (255, 255, 255)


class MainWindow:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        
    def catch_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = GameState.QUIT

    def run(self):
        self.state = GameState.RUNNING
        player = Player((WIN_WIDTH, WIN_HEIGHT))

        while self.state == GameState.RUNNING:
            self.catch_event()

            self.screen.fill(WHITE_BACKGROUND)

            player.draw(self.screen)
            player.handle_keys()

            pygame.display.update()
            #pygame.display.flip()
            #self.clock.tick(100)

        pygame.quit()
