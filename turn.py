from main import map_to_point
from player import Player


class Turn(object):

    current_piece = None
    destination_square = None

    def __init__(self, player):
        # self.player = player

        if player.kind is Player.PlayerKind.HUMAN:
            self.prompt_move(player)
        elif player.kind is Player.PlayerKind.COMPUTER:
            self.calculate_move()

    def prompt_move(self, player):
        # Check if current_piece exists at location
        while self.current_piece is None:
            source_point = map_to_point(input("Move from: "))
            for p in player.piece_list:
                if p.current_square.x == source_point[0] and p.current_square.y == source_point[1]:
                    self.current_piece = p
                    print("piece: {} belongs to player {}".format(
                        source_point, str(player.color)))
                    player.print_pieces()
                    break
            if self.current_piece is None:
                # TODO create a function to print (1,0) as (B1)
                print("No piece belonging to you at location: {}".format(str(source_point)))

        # Check if destination_square is a valid Move
        while self.destination_square is None:
            destination_square = map_to_point(input("Move to: "))
            if self.current_piece.is_move_valid(destination_square):
                self.destination_square = destination_square
            else:
                print("Move to {} with piece at {} is invalid.".format(
                    destination_square, self.current_piece.location))

    def calculate_move(self):
        pass
