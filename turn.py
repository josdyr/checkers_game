from main import map_to_point
from player import Player


class Turn(object):

    # TODO(build and validate mandatory list)

    def __init__(self, player, board):
        self.current_piece = None
        self.destination_square = None
        self.board = board
        self.extra_turn = False

        if player.kind is Player.PlayerKind.HUMAN:
            self.prompt_move(player)
        elif player.kind is Player.PlayerKind.COMPUTER:
            self.calculate_move()

    def prompt_move(self, player):
        # Check if current_piece exists at location
        move_is_valid = False
        while not move_is_valid or self.destination_square is None:
            source_point = map_to_point(input("Move from: "))
            for p in player.piece_list:
                if p.current_square.x == source_point[0] and p.current_square.y == source_point[1]:
                    self.current_piece = p
                    break
            if self.current_piece is None:
                # TODO(create a function to print (1,0) as (B1))
                print("No piece belonging to you at location: {}".format(str(source_point)))
            destination_square = map_to_point(input("Move to: "))
            move_is_valid = self.board.is_move_valid(self.current_piece, destination_square)
            if move_is_valid:
                self.destination_square = destination_square
            else:
                print("Move to {} with piece at {} is invalid.".format(
                    destination_square, str(self.current_piece.current_square))
                )

    def calculate_move(self):
        # TODO()
        pass
