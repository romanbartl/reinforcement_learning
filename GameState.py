from enum import Enum 

class GameState(Enum):
    RUNNING = 0
    PAUSED = 1
    QUIT = 2
    GAME_OVER = 3
    WIN = 4
