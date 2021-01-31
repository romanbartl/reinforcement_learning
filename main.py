from MainWindow import MainWindow
from Environment import Environment
from GameState import GameState
from Actions import Actions


def main():
    # TODO human vs agent play
    '''
    env = Environment()

    while True:
        env.render_scene()
        if env.get_game_state() == GameState.QUIT:
            break
    '''

    '''
    import random
    randomlist = []
    for i in range(0, 1000):
        n = random.choice(list(Actions))
        randomlist.append(n)

    i = 0

    env = Environment(False)

    while i < 1000:
        env.render_scene()
        env.step(randomlist[i])

        i += 1
    '''

    env = Environment()

    while True:
        env.render_scene()
        if env.get_game_state() == GameState.QUIT:
            break


if __name__ == "__main__":
    main()
