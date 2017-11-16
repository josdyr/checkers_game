import string

from main import BOARD_SIZE
from piece import Piece
from player import Player
from square import Square


class Board(object):

    board = [[Square(x, y) for y in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.populate_board()

    def move_piece(self, turn):
        piece = turn.current_piece
        destination = turn.destination_square
        piece.current_square.clear()
        self.board[destination[0]][destination[1]].set_piece(piece)

    def populate_board(self):
        """place all pieces to the board"""
        self.create_player_pieces(self.player1)
        self.create_player_pieces(self.player2)

    def clear(self):
        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                self.board[row][col].clear()

    def create_player_pieces(self, player):
        for row, row_of_squares in enumerate(self.board):
            for col, square in enumerate(row_of_squares):
                for (x, y) in player.initial_points:
                    if row == x and col == y:
                        piece = Piece(player)
                        square.set_piece(piece)

    def draw_board(self):
        for row, row_of_squares in enumerate(self.board):
            print()
            print("{} ".format(row), end='')
            print("{} ".format(row + 1), end='')
            for col, square in enumerate(row_of_squares):
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

    def is_move_valid(self, piece, destination):
        x = piece.current_square.x
        y = piece.current_square.y

        direction = -1
        if piece.player_owner.color == Player.PlayerColor.WHITE:
            direction = 1

        possibility_left = [x + direction, y - 1]
        possibility_right = [x + direction, y + 1]

        if destination == possibility_left or destination == possibility_right:
            return True
        else:
            return False
