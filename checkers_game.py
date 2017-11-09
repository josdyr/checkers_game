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
    coordinates = (None, None)


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
    set_coordinates(board)

    # give points/new coordinates
    set_points(board)
    # initiate pieces:
    place_pieces(board)

    return board


def set_coordinates(board):

    for row_idx, row in enumerate(board):
        for space_idx, space in enumerate(row):

            # give coordinates to each space
            space.coordinates = (row_idx, space_idx)


def set_points(board):
    for row_idx, row in enumerate(board):
        for space_idx, space in enumerate(row):

            # give Points to each space
            space.point = Point(row_idx, space_idx)


def place_pieces(board):

    # white_initial_positions = [
    #     (0, 0), (2, 0), (1, 1), (0, 2), (4, 2), (1, 3), (0, 4), (2, 4), (1, 5), (0, 6), (2, 6), (1, 7)
    # ]
    white_initial_positions = [
        (4, 2)
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

    # return (x, y)
    return Point(x, y)


def move(from_space, to_space):
    coor_from = map_coordinates(from_space)
    print("coor_from", coor_from)
    coor_to = map_coordinates(to_space)
    print("coor_to", coor_to)

    piece = get_board_piece(coor_from)

    # check if space has a from_space
    if piece is not None:
        player = piece.player
        current_type = piece._type

        check_spaces_list = get_checklist(current_type, player)

        valid_move = is_valid_move(coor_from, coor_to, check_spaces_list, player)

        # pdb.set_trace()

        if valid_move:
            do_move(coor_from, coor_to, piece)

            if check_king(coor_to) is True:
                board[coor_to.x][coor_to.y].piece._type = "King"
        else:
            print('Invalid move.')

    else:
        print("Local Error: Current space has no piece")

    draw_board()


def do_move(coor_from, coor_to, piece):
    set_board_piece(coor_to, piece)
    set_board_piece(coor_from, None)


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


def is_valid_move(coor_from, coor_to, check_spaces_list, player):

    # coor_to must have a piece in board
    if board[coor_to.x][coor_to.y].piece:
        print("This space has a piece. Try again")
        return False

    valid_moves = [Point(coor_from.x + point.x, coor_from.y + point.y)
                   for point in check_spaces_list]

    valid_moves = [point for point in valid_moves if point.x
                   >= 0 and point.x < 8 and point.y >= 0 and point.y < 8]

    if coor_to not in valid_moves:
        return False

    if coor_to == coor_from.add(Point(-2, -2)) or coor_to == coor_from.add(Point(-2, 2)):  # if move is two_disp
        if board[coor_to.x][coor_to.y].piece is None:  # if current space has no piece
            board[coor_to.x + 1][coor_to.y + 1].piece = None  # remove the piece in between
            return True

    return True


def game_loop():
    while True:
        draw_board()
        from_space = input('What piece do you want to move from: ')
        to_space = input('What piece do you want to move to: ')
        move(from_space, to_space)


def check_king(coor_to):
    if coor_to.x == 0 or coor_to.x == 7:
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
