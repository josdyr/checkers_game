class Piece(object):

    def __init__(self, player_owner):
        self.player_owner = player_owner
        self.player_owner.add_piece(self)
        self.valid_moves = []
        self.mandatory_moves = []
        self.current_square = None

    def __str__(self):
        return "Position: {}".format(str(self.point))

    def is_move_valid(self, destination):
        # TODO validation
        return True
