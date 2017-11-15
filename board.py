import string

from main import BOARD_SIZE
from piece import Piece
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
        self.player1.print_pieces()
        self.player2.print_pieces()
        self.create_player_pieces(self.player1)
        print("after player1 pieces")
        self.player1.print_pieces()
        self.player2.print_pieces()
        # self.create_player_pieces(self.player2)
        print("after player2 pieces")
        self.player1.print_pieces()
        self.player2.print_pieces()

    def clear(self):
        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                self.board[row][col].clear()

    def create_player_pieces(self, player):
        for row, row_of_squares in enumerate(self.board):
            for col, square in enumerate(row_of_squares):
                import pdb
                # pdb.set_trace()
                for (x, y) in player.initial_points:
                    if row == x and col == y:
                        print("before create piece, player {}, row {}, col {}, x {}, y {}".format(
                            str(player.color), row, col, x, y))
                        self.player1.print_pieces()
                        self.player2.print_pieces()
                        piece = Piece(player)
                        player.add_piece(piece)
                        print("after create piece, row {}, col {}, x {}, y {}".format(row, col, x, y))
                        self.player1.print_pieces()
                        self.player2.print_pieces()
                        square.set_piece(piece)
                        print("after set piece, row {}, col {}, x {}, y {}".format(row, col, x, y))
                        self.player1.print_pieces()
                        self.player2.print_pieces()
                        pdb.set_trace()

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
