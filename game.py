from enum import Enum
import pdb


class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2


class Player(object):

    piece_list = []

    def __init__(self, player_type):
        self.player_type = player_type

    def has_pieces(self):
        if len(self.piece_list) >= 1:
            return True
        else:
            return False


class Game(object):

    turn_list = []

    def __init__(self, player1_type, player2_type):
        self.turn_count = 0
        self.player1 = Player(player1_type)
        self.player2 = Player(player2_type)
        self.board = Board(self.player1, self.player2)
        self.start()

    def start(self):
        # Set the initial player's turn
        self._active_player = self.player1

        while self.player1.has_pieces() and self.player2.has_pieces():
            self.next_turn()
        print("Game Over")

    def next_turn(self):
        print("Turn: {}".format(self.turn_count))
        self.turn_list[self.turn_count] = Turn(self._active_player)

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

        if player.player_type is PlayerType.HUMAN:
            self.prompt_move()
        else:
            self.calculate_move()
        self.piece.move(self.destination)

    def prompt_move(self):
        while self.piece is None:
            piece_from_point = map_coordinates(input("Move from: "))
            for p in self.player.piece_list:
                if p.position == piece_from_point:
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


class Piece(object):
    valid_moves = []

    def __init__(self, position, owner):
        self.position = position
        self.owner = owner

    def __str__(self):
        return "Position: {}".format(str(self.position))

    def move(self, destination):
        self.position = destination

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

    def __init__(self, player1, player2):
        self.player1_positions = [
            Piece(Point(0, 0), player1), Piece(Point(2, 0), player1), Piece(Point(1, 1), player1), Piece(Point(0, 2), player1), Piece(Point(2, 2), player1), Piece(Point(1, 3), player1), Piece(
                Point(0, 4), player1), Piece(Point(2, 4), player1), Piece(Point(1, 5), player1), Piece(Point(0, 6), player1), Piece(Point(2, 6), player1), Piece(Point(1, 7), player1)
        ]
        self.player2_positions = [
            Piece(Point(6, 0), player2), Piece(Point(5, 1), player2), Piece(Point(7, 1), player2), Piece(Point(6, 2), player2), Piece(Point(5, 3), player2), Piece(Point(7, 3), player2), Piece(
                Point(6, 4), player2), Piece(Point(5, 5), player2), Piece(Point(7, 5), player2), Piece(Point(6, 6), player2), Piece(Point(5, 7), player2), Piece(Point(7, 7), player2)
        ]

    def has_pieces():
        pass

    def draw():
        pass


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
    game = Game(PlayerType.HUMAN, PlayerType.COMPUTER)
    pdb.set_trace()


if __name__ == "__main__":
    main()
