import numpy
import os
import pdb
import string


###########
# CLASSES #
###########


class Slot(object):
    piece = None
    location = ""
    coordinates = (None, None)

    def __str__(self):
        return self.location + self.piece.player


class Piece(object):
    player = ""

    def __init__(self, player):
        self.player = player


class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col


# class Player(object):
#     white_player = True
#     pieces = 12
#
#     def __init__(self, white_player, pieces):
#         self.white_player = white_player
#         self.pieces = pieces


#############
# FUNCTIONS #
#############

def make_board():

    board = [[Slot() for j in range(8)] for i in range(8)]

    # give coordinates:
    give_location(board)
    # initiate pieces:
    place_pieces(board)

    return board


def give_location(board):
    # make range 1 - 8
    # numbers = list(range(8))
    numbers = list(range(8, 0, -1))
    # make range A - H
    letters = string.ascii_uppercase[:8]

    for row_idx, row in enumerate(board):
        for slot_idx, slot in enumerate(row):

            # give locations to each slot
            current_location = ""
            current_location += str(letters[slot_idx])
            current_location += str(numbers[row_idx])
            slot.location = current_location

            # give coordinates to each slot
            slot.coordinates = (row_idx, slot_idx)


def place_pieces(board):
    white_initial_positions = ["A1", "A3", "B2", "C1",
                               "C3", "D2", "E1", "E3", "F2", "G1", "G3", "H2"]
    black_initial_positions = ["A7", "B6", "B8", "C7",
                               "D6", "D8", "E7", "F6", "F8", "G7", "H6", "H8"]
    # if location in lists is the same as the slot in board:
    for row_idx, row in enumerate(board):
        for slot_idx, slot in enumerate(row):
            if board[row_idx][slot_idx].location in white_initial_positions:
                board[row_idx][slot_idx].piece = Piece('W')
            elif board[row_idx][slot_idx].location in black_initial_positions:
                board[row_idx][slot_idx].piece = Piece('B')
    return board


def draw_board():
    # os.system('clear')
    for row_idx, row in enumerate(board):
        print("{} ".format(row_idx + 1), end='')  # Print the margin numbers

        # Print '[ ]' OR print the content:
        for slot_idx, slot in enumerate(row):
            if slot.piece:  # if Piece in Slot
                print('[{}]'.format(board[row_idx][slot_idx].piece.player), end="")
            else:
                print("[ ]", end="")
        print("")
    print(" ", end="")

    # Print the characters
    letters = string.ascii_uppercase[:8]
    for l in letters:
        print("  {}".format(l), end="")
    print()


def move(player, piece, to):

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

    from_x = int(piece[1]) - 1  # from_x
    from_y = abc_map[piece[0]]  # from_y
    print("from: ({}, {})".format(from_x, from_y))

    to_x = int(to[1]) - 1
    to_y = abc_map[to[0]]
    print("to: ({}, {})".format(to_x, to_y))

    # check if slot has a piece
    if board[from_x][from_y].piece is not None:
        print("current slot has a piece")
        player = board[from_x][from_y].piece.player
        coor_from = board[from_x][from_y].coordinates
        coor_to = board[to_x][to_y].coordinates

        if player == "W":
            # if 'to-coordinates' is same as ('piece-coordinates' plus the difference)
            if coor_from == tuple(numpy.subtract(coor_to, (-1, 1))) or coor_from == tuple(numpy.subtract(coor_to, (-1, -1))):
                print("This is a valid move diagonally for White!")
                board[from_x][from_y].piece = None  # set piece to None
                board[to_x][to_y].piece = Piece(player)  # make a new Piece
            else:
                print("This is not a valid diagonal move. Try again...")

        elif player == "B":
            # if 'to-coordinates' is same as ('piece-coordinates' plus the difference)
            if coor_from == tuple(numpy.subtract(coor_to, (1, 1))) or coor_from == tuple(numpy.subtract(coor_to, (1, -1))):
                print("This is a valid move diagonally for Black!")
                board[from_x][from_y].piece = None  # set piece to None
                board[to_x][to_y].piece = Piece(player)  # make a new Piece
            else:
                print("This is not a valid diagonal move. Try again...")
    else:
        print("Error: Current slot has no piece")

    draw_board()

    ###########
    # PROGRAM #
    ###########


board = make_board()
draw_board()

pdb.set_trace()

# testing moves:
move('W', 'C6', 'B5')

move('B', 'D3', 'E4')

move('W', 'E6', 'F5')
