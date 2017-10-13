# Class: 2D list that holds the board
board = [[None] * 8] * 8


# Class: Move
class Move():
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player


# Class: Player
class Player:
    color = 'white'
    pieces = 12

    def __init__(self, color, pieces):
        self.color = color
        self.pieces = pieces


def move(move_obj):
    pass


def draw_board():
    for row in board:
        for col in row:
            if col is None:
                print('[ ]', end='')
            else:
                print(col, end='')
        print('')
