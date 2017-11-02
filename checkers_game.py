import string

white_initial_positions = ["A1", "A3", "B2", "C1", "C3", "D2", "E1", "E3", "F2", "G1", "G3", "H2"]
black_initial_positions = ["A7", "B6", "B8", "C7", "D6", "D8", "E7", "F6", "F8", "G7", "H6", "H8"]
board = [[None] * 8 for i in range(8, 0, -1)]


###########
# CLASSES #
###########

class Slot(object):

    # def __init__(self, piece, location):
    #     self.piece = piece
    #     self.location = location
    pass


class Piece(object):

    def __init__(self, color, location, player):
        self.color = color
        self.location = location
        self.player = player


class Point(object):

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move(self, d_row, d_col):
        self.row = self.row + d_row
        self.col = self.col + d_col

    def __str__(self):
        return "Point: {}, {}".format(self.row, self.col)


class Player(object):
    color = None
    pieces = 12

    def __init__(self, color, pieces):
        self.color = color
        self.pieces = pieces


#############
# FUNCTIONS #
#############

def make_board(board):
    for row in board:
        for col in row:
            row[col] = 1

    return board


def draw_board():
    i = 8
    for row in board:
        print("{} ".format(i), end='')  # Print the margin numbers
        i = i - 1

        # Print '[ ]' OR print the content:
        for col in row:
            if col is None:
                print('[ ]', end='')
            else:
                print(col, end='')
        print('')
    print(' ', end="")

    # Print the characters
    alphabet = string.ascii_uppercase[:8]
    for l in alphabet:
        print("  {}".format(l), end="")
    print()
