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


#############
# FUNCTIONS #
#############

def make_board():

    board = [[Slot() for j in range(8)] for i in range(8)]

    # initiate pieces:
    place_pieces(board)

    return board


def place_pieces(board):
    white_initial_positions = ["A1", "A3", "B2", "C1",
                               "C3", "D2", "E1", "E3", "F2", "G1", "G3", "H2"]
    black_initial_positions = ["A7", "B6", "B8", "C7",
                               "D6", "D8", "E7", "F6", "F8", "G7", "H6", "H8"]
    # if location in lists is the same as the slot in board:
    for row_idx, row in enumerate(board):
        for slot_idx, slot in enumerate(row):
            if board[row_idx][slot_idx].location in white_initial_positions:
                board[row_idx][slot_idx] = Piece('W')
            elif board[row_idx][slot_idx].location in black_initial_positions:
                board[row_idx][slot_idx] = Piece('B')
    return board


def draw_board():
    for row_idx, row in enumerate(board):
        print("{} ".format(len(row) - row_idx), end='')  # Print the margin numbers

        # Print '[ ]' OR print the content:
        for slot_idx, slot in enumerate(row):
            if slot.piece:  # if Piece in Slot
                print('[{}]'.format(board[row_idx][slot_idx].piece.player), end="")
            else:
                # print('[{}]'.format(board[row_idx][slot_idx].location), end='')
                print("[ ]", end="")
        print("")
    print(" ", end="")

    # Print the characters
    letters = string.ascii_uppercase[:8]
    for l in letters:
        print("  {}".format(l), end="")
    print()


def move(piece, location):
    abc_map = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8
    }
    piece_letter = abc_map[piece[0]]
    piece_number = int(piece[1])
    print(piece_letter, piece_number)

    location_letter = abc_map[location[0]]
    location_number = int(location[1])
    print(location_letter, location_number)

    board[piece_letter][piece_number].piece = None  # set piece to None
    board[location_letter][location_number].piece = Piece('W')  # make a new Piece

    draw_board()

    ###########
    # PROGRAM #
    ###########


board = make_board()
