import game as g
from player import Player


BOARD_SIZE = 8
NUM_PIECES = 12
debug = False


def map_to_point(arg):

    abc_map = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7
    }

    x = int(arg[1]) - 1
    y = abc_map[arg[0]]

    return [x, y]


def main():
    debug = input("debug-mode? [y/n]: ")

    game = g.Game(Player.PlayerKind.HUMAN, Player.PlayerKind.HUMAN)
    if debug != "y":
        game.start()


if __name__ == "__main__":
    main()
