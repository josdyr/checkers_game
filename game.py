from enum import Enum
import pdb


BOARD_SIZE = 8
NUM_PIECES = 12


class PlayerKind(Enum):
    HUMAN = 1
    COMPUTER = 2


class Player(object):

    owner = None

    def __init__(self, kind, piece_list):
        self.kind = kind
        self.piece_list = piece_list

    def has_pieces(self):
        if len(self.piece_list) >= 1:
            return True
        else:
            return False


class Game(object):

    turn_list = []

    def __init__(self, player1_kind, player2_kind):
        self.turn_count = 0
        self.player1 = Player(player1_kind, PLAYER1_PIECES)
        self.player2 = Player(player2_kind, PLAYER2_PIECES)
        self.board = Board(self.player1, self.player2)
        self.board.populate_board(self.player1)
        self.board.populate_board(self.player2)
        self.start()

    def start(self):
        # Set the initial player's turn
        self._active_player = self.player1

        while self.player1.has_pieces() and self.player2.has_pieces():
            self.next_turn()
        print("Game Over")

    def next_turn(self):
        print("Turn: {}".format(self.turn_count))
        self.turn_list.append(Turn(self._active_player))

        # Switch player
        if self._active_player is self.player1:
            self._active_player = self.player2
        else:
            self._active_player = self.player1
        # And increment the turn_count
        self.turn_count += 1


class Turn(object):

    piece = None
    destination = None

    def __init__(self, player):
        self.player = player

        if player.kind is PlayerKind.HUMAN:
            self.prompt_move()
        else:
            self.calculate_move()
        self.piece.move(self.destination)

    def prompt_move(self):
        while self.piece is None:
            pdb.set_trace()
            piece_from_point = map_coordinates(input("Move from: "))
            for p in self.player.piece_list:
                if p.point == piece_from_point:
                    self.piece = p
                    break
            if self.piece is None:
                print("No piece belonging to you at location: {}".format(str(piece_from_point)))
        while self.destination is None:
            piece_to_point = map_coordinates(input("Move to: "))
            if self.piece.is_move_valid(piece_to_point):
                self.destination = piece_to_point
            else:
                print("Move to {} with piece at {} is invalid.".format(
                    piece_to_point, self.piece.location))

    def calculate_move(self):
        pass


class Move(object):

    def __init__(self):
        self.piece = None
        self.destination = None


class Piece(object):
    valid_moves = []
    mandatory_moves = []

    def __init__(self, point):
        self.point = point

    def __str__(self):
        return "Position: {}".format(str(self.point))

    def move(self, destination):
        self.point = destination

    def is_move_valid(self, destination):
        return True


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Board(object):

    board = [[None] * BOARD_SIZE] * BOARD_SIZE

    def __init__(self, player1, player2):
        pass

    def populate_board(self, player1):
        """place all pieces to the board"""
        for piece in player1.piece_list:
            for i, row in enumerate(self.board):
                for j, col in enumerate(row):
                    if i == piece.point.x and j == piece.point.y:
                        self.board[i][j] = piece
        pass

    def has_pieces():
        pass

    def draw(self, board):
        for space in board:
            if space.piece is None:
                print("[ ]")
            else:
                print("[P]")


PLAYER1_PIECES = [
    Piece(Point(0, 0)), Piece(Point(2, 0)), Piece(Point(1, 1)), Piece(Point(0, 2)), Piece(Point(2, 2)), Piece(Point(1, 3)), Piece(
        Point(0, 4)), Piece(Point(2, 4)), Piece(Point(1, 5)), Piece(Point(0, 6)), Piece(Point(2, 6)), Piece(Point(1, 7))]

PLAYER2_PIECES = [
    Piece(Point(6, 0)), Piece(Point(5, 1)), Piece(Point(7, 1)), Piece(Point(6, 2)), Piece(Point(5, 3)), Piece(Point(7, 3)), Piece(
        Point(6, 4)), Piece(Point(5, 5)), Piece(Point(7, 5)), Piece(Point(6, 6)), Piece(Point(5, 7)), Piece(Point(7, 7))]


def map_coordinates(arg):

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

    y = int(arg[1]) + 1
    x = abc_map[arg[0]]

    return Point(x, y)


def main():
    # TODO Promt user for player types
    game = Game(PlayerKind.HUMAN, PlayerKind.HUMAN)
    pdb.set_trace()
    pass


if __name__ == "__main__":
    main()
