white_initial_positions = [
    "A1", "A3", "B2", "C1", "C3", "D2", "E1", "E3", "F2", "G1", "G3", "H2"
]
black_initial_positions = [
    "A7", "B6", "B8", "C7", "D6", "D8", "E7", "F6", "F8", "G7", "H6", "H8"
]


board = [[None] * 8] * 8
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]


class Slot(object):
    pass


# Creates a coordinate. Methods: move
class Point(object):

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move(self, d_row, d_col):
        self.row = self.row + d_row
        self.col = self.col + d_col

    def __str__(self):
        return "Point: {}, {}".format(self.row, self.col)


class Piece(object):
    position = ""
    location = Point()

    def __init__(self, color, position):
        self.color = color
        self.position = position


class Move(object):
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player


class Player(object):
    color = 'white'
    pieces = 12

    def __init__(self, color, pieces):
        self.color = color
        self.pieces = pieces


def draw_board():
    i = 8
    for row in board:
        print("{} ".format(i), end='')
        i = i - 1
        for col in row:
            if col is None:
                print('[ ]', end='')
            else:
                print(col, end='')
        print('')
    print(' ', end="")
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for l in alphabet:
        print("  {}".format(l), end="")
    print()
