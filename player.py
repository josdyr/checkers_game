from enum import Enum


class Player(object):

    color = None
    piece_list = []

    PLAYER1_POINTS = [
        [0, 0], [2, 0], [1, 1], [0, 2], [2, 2], [1, 3],
        [0, 4], [2, 4], [1, 5], [0, 6], [2, 6], [1, 7]
    ]

    PLAYER2_POINTS = [
        [6, 0], [5, 1], [7, 1], [6, 2], [5, 3], [7, 3],
        [6, 4], [5, 5], [7, 5], [6, 6], [5, 7], [7, 7]
    ]

    def __init__(self, kind, color, initial_points):
        self.kind = kind
        self.color = color
        self.initial_points = initial_points

    def print_pieces(self):
        for p1 in self.piece_list:
            print("Player: {}, Piece: {}".format(str(self.color), str(p1.current_square)))

    def has_pieces(self):
        if len(self.piece_list) > 0:
            return True
        else:
            return False

    def add_piece(self, piece):
        self.piece_list.append(piece)

    class PlayerColor(Enum):
        WHITE = "W"
        BLACK = "B"

        def __str__(self):
            return str(self.value)

    class PlayerKind(Enum):
        HUMAN = 1
        COMPUTER = 2
