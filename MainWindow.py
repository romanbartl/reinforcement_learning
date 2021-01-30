import pygame
from GameState import GameState


WIN_WIDTH = 500
WIN_HEIGHT = 500

WHITE_BACKGROUND = (255, 255, 255)


class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        self.screen.fill(WHITE_BACKGROUND)

    def catch_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = GameState.QUIT

    def run(self):
        self.state = GameState.RUNNING

        while self.state == GameState.RUNNING:
            self.catch_event()

            pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
            pygame.display.flip()

        pygame.quit()
