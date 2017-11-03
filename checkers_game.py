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
    for row_idx, row in enumerate(board):
        print("{} ".format(row_idx + 1), end='')  # Print the margin numbers

        # Print '[ ]' OR print the content:
        for slot_idx, slot in enumerate(row):
            if slot.piece:  # if Piece in Slot
                print('[{}   ]'.format(board[row_idx][slot_idx].piece.player), end="")
            else:
                # print('[{}]'.format(board[row_idx][slot_idx].location), end='')
                print("[{}]".format(str(row_idx) + ", " + str(slot_idx)), end="")
        print("")
    print(" ", end="")

    # Print the characters
    letters = string.ascii_uppercase[:8]
    for l in letters:
        print("   {}  ".format(l), end="")
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
    print("x: {}, y: {}".format(from_x, from_y))

    to_x = int(to[1]) - 1
    to_y = abc_map[to[0]]
    print("x: {}, y: {}".format(to_x, to_y))

    board[from_x][from_y].piece = None  # set piece to None
    board[to_x][to_y].piece = Piece('C')  # make a new Piece

    draw_board()

    ###########
    # PROGRAM #
    ###########


board = make_board()
