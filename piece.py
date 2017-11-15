class Piece(object):

    valid_moves = []
    mandatory_moves = []
    current_square = None

    def __init__(self, player_owner):
        self.player_owner = player_owner

    def __str__(self):
        return "Position: {}".format(str(self.point))

    def is_move_valid(self, destination):
        return True
