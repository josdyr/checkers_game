import os
import pdb
import string


###########
# CLASSES #
###########


class Space(object):
    piece = None
    coordinates = (None, None)


class Piece(object):
    player = ""
    _type = None

    def __init__(self, _type):
        self.player = _type

    def get_display_value(self):
        if self._type is None:
            return self.player[0]
        else:
            return self._type[0]


class Player(object):
    pass


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

    for row_idx, row in enumerate(board):
        for space_idx, space in enumerate(row):

            # give coordinates to each space
            space.coordinates = (row_idx, space_idx)


def place_pieces(board):

    white_initial_positions = [
        (0, 0), (2, 0), (1, 1), (0, 2), (2, 2), (1, 3), (0, 4), (2, 4), (1, 5), (0, 6), (2, 6), (1, 7)
    ]
    black_initial_positions = [
        (6, 0), (5, 1), (7, 1), (6, 2), (5, 3), (7, 3), (6, 4), (5, 5), (7, 5), (6, 6), (5, 7), (7, 7)
    ]

    # if location in lists is the same as the space in board:
    for row_idx, row in enumerate(board):
        for space_idx, space in enumerate(row):
            if board[row_idx][space_idx].coordinates in white_initial_positions:
                board[row_idx][space_idx].piece = Piece('White')
            elif board[row_idx][space_idx].coordinates in black_initial_positions:
                board[row_idx][space_idx].piece = Piece('Black')
    return board


def draw_board():
    # os.system('clear')
    for row_idx, row in enumerate(board):
        print("{} ".format(row_idx), end='')  # Print the index number (debug)
        print("{} ".format(row_idx + 1), end='')  # Print the margin game-numbers

        # Print '[ ]' OR print the content:
        for space_idx, space in enumerate(row):
            if space.piece:  # if Piece in space
                print('[{}]'.format(board[row_idx][space_idx].piece.get_display_value()), end="")
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


def get_board_piece(coor):
    return board[coor[0]][coor[1]].piece


def set_board_piece(coor, value):
    board[coor[0]][coor[1]].piece = value


def map_coordinates(arg):

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

    return (x, y)


def move(from_space, to_space):

    # pdb.set_trace()

    coor_from = map_coordinates(from_space)
    print(coor_from)
    coor_to = map_coordinates(to_space)
    piece = get_board_piece(coor_from)

    # check if space has a from_space
    if piece is not None:
        player = piece.player
        current_type = piece._type

        # make king a type variable
        # make a get_dispacements(type, player)
        displacements = get_dispacements(current_type, player)

        # get_valid_moves(coor_from, displacements)
        valid_moves = get_valid_moves(coor_from, displacements)

        if coor_to in valid_moves:
            do_move(coor_from, coor_to, piece)

            if check_king(coor_to) is True:
                board[coor_to[0]][coor_to[1]].piece._type = "King"
        else:
            print('Invalid move.')

    else:
        print("Local Error: Current space has no piece")


def do_move(coor_from, coor_to, piece):
    set_board_piece(coor_to, piece)
    set_board_piece(coor_from, None)


def get_dispacements(current_type, player):
    if current_type == "king":
        displacements = [(-1, -1), (-1, 1), (1, 1), (1, -1), (-2, -2), (-2, 2), (2, 2), (2, -2)]
    elif player == "White":
        displacements = [(1, -1), (1, 1), (2, -2), (2, 2)]
    elif player == "Black":
        displacements = [(-1, -1), (-1, 1), (-2, -2), (-2, 2)]
    return displacements


def get_valid_moves(coor_from, displacements):
    valid_moves = [(coor_from[0] + coor[0], coor_from[1] + coor[1])
                   for coor in displacements]
    valid_moves = [coor for coor in valid_moves if coor[0]
                   >= 0 and coor[0] < 8 and coor[1] >= 0 and coor[1] < 8]
    return valid_moves


def game_loop():
    while True:
        draw_board()
        from_space = input('What piece do you want to move from: ')
        to_space = input('What piece do you want to move to: ')
        move(from_space, to_space)


def check_king(coor_to):
    pdb.set_trace()
    if coor_to[0] == 0 or coor_to[0] == 7:
        return True
    else:
        return False

    ###########
    # PROGRAM #
    ###########


board = make_board()

move('B6', 'C5')
move('C5', 'B4')
move('B4', 'C3')
move('C3', 'B2')
move('B2', 'C1')

draw_board()

# game_loop()
