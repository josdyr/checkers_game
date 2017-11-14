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
    piece_list = []

    def __init__(self, kind, color, initial_points):
        self.kind = kind
        self.color = color
        self.populate_piece_list(initial_points)

    def has_pieces(self):
        if len(self.piece_list) >= 1:
            return True
        else:
            return False

    def add_piece(self, piece):
        self.piece_list.append(piece)

    def populate_piece_list(self, point_list):
        for point in point_list:
            self.add_piece(Piece(point, self))


class Game(object):

    turn_list = []

    def __init__(self, player1_kind, player2_kind):
        self.turn_count = 0
        self.player1 = Player(player1_kind, PlayerColor.WHITE, PLAYER1_POINTS)
        self.player2 = Player(player2_kind, PlayerColor.BLACK, PLAYER2_POINTS)
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
        current_turn = Turn(self._active_player)
        # DOMOVE:
        self.board.move_piece(current_turn.piece, current_turn.destination)
        self.turn_list.append(current_turn)

        # Switch player
        if self._active_player is self.player1:
            self._active_player = self.player2
        else:
            self._active_player = self.player1
        # And increment the turn_count
        self.turn_count += 1

    # def get_square(self, point):
    #     return self.board[point.x][point.y]


class Turn(object):

    piece = None
    destination = None

    def __init__(self, player):
        self.player = player

        if player.kind is PlayerKind.HUMAN:
            self.prompt_move()
        elif player.kind is PlayerKind.COMPUTER:
            self.calculate_move()

    def prompt_move(self):
        # Check if piece exists at location
        while self.piece is None:
            source_point = map_to_point(input("Move from: "))
            for p in self.player.piece_list:
                if p.current_square.point == source_point:
                    self.piece = p
                    break
            if self.piece is None:
                print("No piece belonging to you at location: {}".format(str(source_point)))
        # Check if destination is a valid Move
        while self.destination is None:
            destination_point = map_to_point(input("Move to: "))
            if self.piece.is_move_valid(destination_point):

                self.destination = destination_point
            else:
                print("Move to {} with piece at {} is invalid.".format(
                    destination_point, self.piece.location))

    def calculate_move(self):
        pass


class Piece(object):

    valid_moves = []
    mandatory_moves = []
    current_square = None

    def __init__(self, point, owner):
        # self.set_point(point)
        self.owner = owner
        # self.set_current_square(point)

    def __str__(self):
        return "Position: {}".format(str(self.point))

    def is_move_valid(self, destination):
        return True

    # def set_point(self, destination):
    #     self.point = destination


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
    point = None

    def __init__(self, point):
        self.point = point

    def set_piece(self, piece, point):
        self.piece = piece
        self.piece.current_square = self
        # self.point = point
        # self.piece.set_point(self.point)

    def clear(self):
        self.piece = None

    def draw_item(self):
        if self.piece is None:
            print("[ ]", end='')
        else:
            print("[{}]".format(str(self.piece.owner.color)), end='')


class Board(object):

    board = [[Square(Point(x, y)) for y in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.populate_board()

    def move_piece(self, piece, to):
        pdb.set_trace()
        # self.board[to.x][to.y].piece = piece
        # self.board[piece.point.x][piece.point.y].piece = None
        self.board[to.x][to.y].set_piece(piece)
        piece.current_square = self.board[to.x][to.y]

    def populate_board(self):
        """place all pieces to the board"""
        # self.clear()
        self.populate_player_pieces(self.player1)
        self.populate_player_pieces(self.player2)

    def clear(self):
        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                self.board[row][col].clear()

    def populate_player_pieces(self, player):
        for piece in player.piece_list:
            self.board[piece.point.x][piece.point.y].set_piece(piece)

    def draw_board(self):
        for row in range(0, BOARD_SIZE):
            print()
            print("{} ".format(row), end='')
            print("{} ".format(row + 1), end='')
            for col in range(0, BOARD_SIZE):
                self.board[row][col].draw_item()
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


PLAYER1_POINTS = [
    Point(0, 0), Point(2, 0), Point(1, 1), Point(0, 2), Point(2, 2), Point(1, 3),
    Point(0, 4), Point(2, 4), Point(1, 5), Point(0, 6), Point(2, 6), Point(1, 7)]

PLAYER2_POINTS = [
    Point(6, 0), Point(5, 1), Point(7, 1), Point(6, 2), Point(5, 3), Point(7, 3),
    Point(6, 4), Point(5, 5), Point(7, 5), Point(6, 6), Point(5, 7), Point(7, 7)]


def map_to_point(arg):

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
