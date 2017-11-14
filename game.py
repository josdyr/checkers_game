from enum import Enum
import pdb
import string


BOARD_SIZE = 8
NUM_PIECES = 12


class PlayerColor(Enum):
    WHITE = "W"
    BLACK = "B"

    def __str__(self):
        return str(self.value)


class PlayerKind(Enum):
    HUMAN = 1
    COMPUTER = 2


class Player(object):

    owner = None
    color = None

    def __init__(self, kind, color, piece_list):
        self.kind = kind
        self.color = color
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
        self.player1 = Player(player1_kind, PlayerColor.WHITE, PLAYER1_PIECES)
        self.player2 = Player(player2_kind, PlayerColor.BLACK, PLAYER2_PIECES)
        self.board = Board(self.player1, self.player2)

    def start(self):
        # Set the initial player's turn
        self._active_player = self.player1
        self.board.draw_board()

        while self.player1.has_pieces() and self.player2.has_pieces():
            self.next_turn()
            self.board.draw_board()

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
        elif player.kind is PlayerKind.COMPUTER:
            self.calculate_move()

        self.piece.move(self.destination)

    def prompt_move(self):
        # Check if piece exists at location
        while self.piece is None:
            piece_from_point = map_coordinates(input("Move from: "))
            for p in self.player.piece_list:
                if p.point == piece_from_point:
                    self.piece = p
                    break
            if self.piece is None:
                print("No piece belonging to you at location: {}".format(str(piece_from_point)))
        # Check if destination is a valid Move
        while self.destination is None:
            piece_to_point = map_coordinates(input("Move to: "))
            if self.piece.is_move_valid(piece_to_point):
                self.destination = piece_to_point
            else:
                print("Move to {} with piece at {} is invalid.".format(
                    piece_to_point, self.piece.location))

    def calculate_move(self):
        pass


class Piece(object):
    valid_moves = []
    mandatory_moves = []

    def __init__(self, point):
        self.point = point

    def __str__(self):
        return "Position: {}".format(str(self.point))

    # def move(self, destination):
    #     # self.point = destination
    #
    #     pdb.set_trace()

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


class Square(object):

    piece = None
    player = None

    def populate(self, piece, player):
        self.piece = piece
        self.player = player

    def clear(self):
        self.piece = None
        self.player = None

    def draw(self):
        if self.piece is None:
            print("[ ]", end='')
        else:
            print("[{}]".format(str(self.player.color)), end='')


class Board(object):

    board = [[Square() for i in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.populate_board()

    def move(self, from, to):
        # self.point = destination
        pass
        pdb.set_trace()

    def populate_board(self):
        """place all pieces to the board"""
        # self.clear()
        self.populate_player_squares(self.player1)
        self.populate_player_squares(self.player2)

    def clear(self):
        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                self.board[row][col].clear()

    def populate_player_squares(self, player):
        for piece in player.piece_list:
            self.board[piece.point.x][piece.point.y].populate(piece, player)

    def draw_board(self):
        for row in range(0, BOARD_SIZE):
            print()
            print("{} ".format(row), end='')
            print("{} ".format(row + 1), end='')
            for col in range(0, BOARD_SIZE):
                self.board[row][col].draw()
        print()
        print("   ", end='')
        letters = string.ascii_uppercase[:8]
        for l in letters:
            print("  {}".format(l), end="")
        print()
        print("   ", end='')
        for row in range(0, BOARD_SIZE):
            print("  {}".format(row), end="")
        print()


PLAYER1_PIECES = [
    Piece(Point(0, 0)), Piece(Point(2, 0)), Piece(Point(1, 1)), Piece(Point(0, 2)), Piece(Point(2, 2)), Piece(Point(1, 3)), Piece(
        Point(0, 4)), Piece(Point(2, 4)), Piece(Point(1, 5)), Piece(Point(0, 6)), Piece(Point(2, 6)), Piece(Point(1, 7))]

PLAYER2_PIECES = [
    Piece(Point(6, 0)), Piece(Point(5, 1)), Piece(Point(7, 1)), Piece(Point(6, 2)), Piece(Point(5, 3)), Piece(Point(7, 3)), Piece(
        Point(6, 4)), Piece(Point(5, 5)), Piece(Point(7, 5)), Piece(Point(6, 6)), Piece(Point(5, 7)), Piece(Point(7, 7))]


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


def main():
    # TODO Promt user for player types
    game = Game(PlayerKind.HUMAN, PlayerKind.HUMAN)
    pdb.set_trace()
    game.start()


if __name__ == "__main__":
    main()
