import numpy
import os
import pdb
import string


###########
# CLASSES #
###########


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Space(object):
    piece = None
    point = Point(None, None)
    # coordinates = (None, None)


class Piece(object):
    player = ""
    _type = None
    valid_moves = []

    def __init__(self, _type):
        self.player = _type

    def get_display_value(self):
        if self._type is None:
            return self.player[0]
        else:
            return self._type[0]


#############
# FUNCTIONS #
#############

def make_board():

    board = [[Space() for j in range(8)] for i in range(8)]

    # give coordinates:
    # set_coordinates(board)

    # give points/new coordinates
    set_points(board)
    # initiate pieces:
    place_pieces(board)

    return board


# def set_coordinates(board):
#
#     for row_idx, row in enumerate(board):
#         for space_idx, space in enumerate(row):
#
#             # give coordinates to each space
#             space.coordinates = (row_idx, space_idx)


def set_points(board):
    for row_idx, row in enumerate(board):
        for space_idx, space in enumerate(row):

            # give Points to each space
            space.point = Point(row_idx, space_idx)


def place_pieces(board):

    white_initial_positions = [
        Point(0, 0), Point(2, 0), Point(1, 1), Point(0, 2), Point(2, 2), Point(1, 3), Point(
            0, 4), Point(2, 4), Point(1, 5), Point(0, 6), Point(2, 6), Point(1, 7)
    ]
    black_initial_positions = [
        Point(6, 0), Point(5, 1), Point(7, 1), Point(6, 2), Point(5, 3), Point(7, 3), Point(
            6, 4), Point(5, 5), Point(7, 5), Point(6, 6), Point(5, 7), Point(7, 7)
    ]

    # if location in lists is the same as the space in board:
    for row_idx, row in enumerate(board):
        for space_idx, space in enumerate(row):
            if board[row_idx][space_idx].point in white_initial_positions:
                board[row_idx][space_idx].piece = Piece('White')
            elif board[row_idx][space_idx].point in black_initial_positions:
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
    return board[coor.x][coor.y].piece


def set_board_piece(coor, value):
    board[coor.x][coor.y].piece = value


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

    return Point(x, y)


def move(from_space, to_space):
    point_from = map_coordinates(from_space)
    point_to = map_coordinates(to_space)
    print("point_from: {}".format(point_from))
    print("point_to: {}".format(point_to))

    piece = get_board_piece(point_from)

    if piece:
        player = piece.player
        current_type = piece._type

        check_spaces_list = get_checklist(current_type, player)

        valid_moves = set_valid_moves(piece, point_from, point_to, check_spaces_list)

        # print("valid_moves: ", end='')
        # [print("({})".format(valid_move), end='') for valid_move in valid_moves]
        # print()

        valid_move = is_valid_move(piece, point_to, valid_moves)

        if valid_move:
            do_move(point_from, point_to, piece)

            if check_king(point_to) is True:
                board[point_to.x][point_to.y].piece._type = "King"
        else:
            print('Invalid move.')

    else:
        print("Local Error: Current space has no piece")

    draw_board()


def do_move(point_from, point_to, piece):
    set_board_piece(point_to, piece)
    set_board_piece(point_from, None)


def get_checklist(current_type, player):
    if current_type == "king":
        relative = [(-1, -1), (-1, 1), (1, 1), (1, -1), (-2, -2), (-2, 2), (2, 2), (2, -2)]
        check_spaces_list = [Point(r[0], r[1]) for r in relative]
    elif player == "White":
        relative = [(1, -1), (1, 1), (2, -2), (2, 2)]
        check_spaces_list = [Point(r[0], r[1]) for r in relative]
    elif player == "Black":
        relative = [(-1, -1), (-1, 1), (-2, -2), (-2, 2)]
        check_spaces_list = [Point(r[0], r[1]) for r in relative]

    return check_spaces_list


def set_valid_moves(piece, point_from, point_to, check_spaces_list):

    piece.valid_moves = [Point(point_from.x + p.x, point_from.y + p.y)
                         for p in check_spaces_list]

    piece.valid_moves = [p for p in piece.valid_moves if p.x
                         >= 0 and p.x < 8 and p.y >= 0 and p.y < 8]

    # if move is two_disp
    if point_to == point_from.add(Point(-2, -2)) or point_to == point_from.add(Point(-2, 2)):
        if board[point_to.x][point_to.y].piece is None:  # if current space has no piece
            board[point_to.x + 1][point_to.y + 1].piece = None  # remove the piece in between
            # add point to piece.valid_moves
            piece.valid_moves = point_to
    elif point_to == point_from.add(Point(-1, -1)) or point_to == point_from.add(Point(-1, 1)):
        pass

    return piece.valid_moves


def is_valid_move(piece, point_to, valid_moves):

    # point_to must have a piece in board
    if board[point_to.x][point_to.y].piece:
        print("This space has a piece. Try again")
        return False

    # pdb.set_trace()

    return True


def game_loop():
    while True:
        draw_board()
        from_space = input('What piece do you want to move from: ')
        to_space = input('What piece do you want to move to: ')
        move(from_space, to_space)


def check_king(point_to):
    if point_to.x == 0 or point_to.x == 7:
        return True
    else:
        return False

###########
# PROGRAM #
###########


board = make_board()

# move('D6', 'E5')
# move('E5', 'D4')
# move('D4', 'E3')
# move('E3', 'D2')
# move('D2', 'E1')


# draw_board()

# game_loop()
