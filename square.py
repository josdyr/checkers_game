class Square(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None

    def set_piece(self, piece):
        self.piece = piece
        self.piece.current_square = self

    def clear(self):
        self.piece = None

    def draw_item(self):
        if self.piece is None:
            print("[ ]", end='')
        else:
            print("[{}]".format(str(self.piece.player_owner.color)), end='')

    def __str__(self):
        return "{}, {}".format(str(self.x), str(self.y))
