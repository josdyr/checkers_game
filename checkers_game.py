import numpy
import os
import pdb
import string


###########
# CLASSES #
###########


class Space(object):
    piece = None
    location = ""
    coordinates = (None, None)


class Piece(object):
    player = ""
    king = False

    def __init__(self, player):
        self.player = player


#############
# FUNCTIONS #
#############

def make_board():

    board = [[Space() for j in range(8)] for i in range(8)]

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
        for space_idx, space in enumerate(row):

            # give locations to each space
            current_location = ""
            current_location += str(letters[space_idx])
            current_location += str(numbers[row_idx])
            space.location = current_location

            # give coordinates to each space
            space.coordinates = (row_idx, space_idx)


def place_pieces(board):
    white_initial_positions = ["A1", "A3", "B2", "C1",
                               "C3", "D2", "E1", "E3", "F2", "G1", "G3", "H2"]
    black_initial_positions = ["A7", "B6", "B8", "C7",
                               "D6", "D8", "E7", "F6", "F8", "G7", "H6", "H8"]

    # white_initial_positions = [
    #     (0, 0), (2, 0), (1, 1), (0, 2), (2, 2), (1, 3), (0, 4), (2, 4), (1, 5), (0, 6), (2, 6), (1, 7)
    # ]
    # black_initial_positions = [
    #     (6, 0), (5, 1), (7, 1), (6, 2), (5, 3), (7, 3), (6, 4), (5, 5), (7, 5), (6, 6), (5, 7), (7, 7)
    # ]
    #
    # for location in white_initial_positions:
    #     board[location[0]][location[1]].piece = Piece("White")
    #
    # for location in black_initial_positions:
    #     board[location[0]][location[1]].piece = Piece("Black")

    # if location in lists is the same as the space in board:
    for row_idx, row in enumerate(board):
        for space_idx, space in enumerate(row):
            if board[row_idx][space_idx].location in white_initial_positions:
                board[row_idx][space_idx].piece = Piece('White')
            elif board[row_idx][space_idx].location in black_initial_positions:
                board[row_idx][space_idx].piece = Piece('Black')
    return board


def draw_board():
    os.system('clear')
    for row_idx, row in enumerate(board):
        print("{} ".format(row_idx), end='')  # Print the index number (debug)
        print("{} ".format(row_idx + 1), end='')  # Print the margin game-numbers

        # Print '[ ]' OR print the content:
        for space_idx, space in enumerate(row):
            if space.piece:  # if Piece in space
                print('[{}]'.format(board[row_idx][space_idx].piece.player[0]), end="")
            else:
                print("[ ]", end="")
        print("")
    print("   ", end="")

    # Print the characters
    letters = string.ascii_uppercase[:8]
    for l in letters:
        print("  {}".format(l), end="")

    print()
    print("   ", end="")

    for l_idx, l in enumerate(letters):
        print("  {}".format(l_idx), end="")
    print()


def move(piece, to):

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

    to_x = int(to[1]) - 1
    to_y = abc_map[to[0]]

    # check if space has a piece
    if board[from_x][from_y].piece is not None:

        player = board[from_x][from_y].piece.player
        king = board[from_x][from_y].piece.king
        coor_from = board[from_x][from_y].coordinates
        coor_to = board[to_x][to_y].coordinates

        if king:
            displacements = [(-1, -1), (-1, 1), (1, 1), (1, -1), (-2, -2), (-2, 2), (2, 2), (2, -2)]

        if player == "White":
            displacements = [(-1, -1), (-1, 1), (-2, -2), (-2, 2)]

            # # for each displacement, add it to the from locaiton
            # # Generates a list of all possible moves
            # possibleLocations = [(piece[0] + x[0], piece[1] + x[1]) for x in displacements]
            # possibleLocations = [x for x in possibleLocations if x[0]
            #                      >= 0 and x[0] < 8 and x[1] >= 0 and x[1] < 8]
            # if to in possibleLocations:
            #     # Move is valid!
            #     do_move(from_x, from_y, to_x, to_y, player)
            # # if coor_from == tuple(numpy.subtract(coor_to, (-1, 1))) or coor_from == tuple(numpy.subtract(coor_to, (-1, -1))):
            # #    do_move(from_x, from_y, to_x, to_y, player)

            if coor_from == tuple(numpy.subtract(coor_to, (-1, 1))) or coor_from == tuple(numpy.subtract(coor_to, (-1, -1))):
                do_move(from_x, from_y, to_x, to_y, player)

        elif player == "Black":
            displacements = [(1, 1), (1, -1), (2, 2), (2, -2)]

            if coor_from == tuple(numpy.subtract(coor_to, (1, 1))) or coor_from == tuple(numpy.subtract(coor_to, (1, -1))):
                do_move(from_x, from_y, to_x, to_y, player)
    else:
        print("Error: Current space has no piece")

    draw_board()
    print("from: ({}, {})".format(from_x, from_y))
    print("to: ({}, {})".format(to_x, to_y))


def do_move(from_x, from_y, to_x, to_y, player):
    board[from_x][from_y].piece = None  # set piece to None
    board[to_x][to_y].piece = Piece(player)  # make a new Piece


def possible_moves(piece):
    """returns a list of possible moves"""
    pass


def _move(space, to):
    pass

    ###########
    # PROGRAM #
    ###########


board = make_board()
draw_board()

pdb.set_trace()

# testing moves:
move('C6', 'B5')

move('D3', 'E4')

move('E6', 'F5')
