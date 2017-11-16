from board import Board
from player import Player
from turn import Turn


class Game(object):

    turn_list = []

    def __init__(self, player1_kind, player2_kind):
        self.turn_count = 0
        self.player1 = Player(player1_kind, Player.PlayerColor.WHITE)
        self.player2 = Player(player2_kind, Player.PlayerColor.BLACK)
        self.board = Board(self.player1, self.player2)
        self._active_player = self.player1

    def start(self):
        while self.player1.has_pieces() and self.player2.has_pieces():
            self.board.draw_board()
            self.next_turn()
        self.board.draw_board()
        print("Game Over")

    def next_turn(self):
        print("Turn: {}. Active Player: {}".format(self.turn_count, str(self._active_player.color)))
        current_turn = Turn(self._active_player, self.board)
        # DOMOVE:
        self.board.move_piece(current_turn)
        self.turn_list.append(current_turn)

        # Switch player
        if not current_turn.extra_turn:
            if self._active_player is self.player1:
                self._active_player = self.player2
            else:
                self._active_player = self.player1
        # And increment the turn_count
        self.turn_count += 1

    def get_square(self, point):
        return self.board[point.x][point.y]
