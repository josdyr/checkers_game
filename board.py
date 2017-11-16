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
        if abs(piece.current_square.y - destination[1]) == 2:
            self.remove_piece_if_jump(piece, destination)

        piece.current_square.clear()
        self.board[destination[0]][destination[1]].set_piece(piece)

    def remove_piece_if_jump(self, piece, destination):
        x = piece.current_square.x
        y = piece.current_square.y

        if piece.player_owner.color == Player.PlayerColor.WHITE:
            direction_x = (1)
        else:
            direction_x = (-1)

        jump_right = (
            destination[0] == self.board[x + (direction_x * 2)][y + 2].x
            and destination[1] == self.board[x + (direction_x * 2)][y + 2].y
        )

        jump_left = (
            destination[0] == self.board[x + (direction_x * 2)][y - 2].x
            and destination[1] == self.board[x + (direction_x * 2)][y - 2].y
        )

        if jump_right:
            self.board[x + direction_x][y + 1].piece.current_square.clear()

        if jump_left:
            self.board[x + direction_x][y - 1].piece.current_square.clear()

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

        if piece.player_owner.color == Player.PlayerColor.WHITE:
            direction_x = (1)
        else:
            direction_x = (-1)

        is_mandatory_move_right = (
            x + direction_x * 2 >= 0 and x + direction_x * 2 <= 7
            and y + 2 <= 7
            and self.board[x + direction_x][y + 1].piece is not None
            and self.board[x + direction_x][y + 1].piece.player_owner is not piece.player_owner
            and self.board[x + (direction_x * 2)][y + 2].piece is None
        )

        is_mandatory_move_left = (
            x + direction_x * 2 >= 0 and x + direction_x * 2 <= 7
            and y - 2 >= 0
            and self.board[x + direction_x][y - 1].piece is not None
            and self.board[x + direction_x][y - 1].piece.player_owner is not piece.player_owner
            and self.board[x + (direction_x * 2)][y - 2].piece is None
        )

        jump_right = (
            destination[0] == x + (direction_x * 2)
            and destination[1] == y + 2
        )

        jump_left = (
            destination[0] == x + (direction_x * 2)
            and destination[1] == y - 2
        )

        import pdb
        pdb.set_trace()

        if is_mandatory_move_left or is_mandatory_move_right:
            if is_mandatory_move_left and jump_left:
                return True
            if is_mandatory_move_right and jump_right:
                return True
            return False

        possibility_right = (
            x + direction_x >= 0 and x + direction_x <= 7
            and y + 1 <= 7
            and self.board[x + (direction_x * 1)][y + 1].piece is None
        )
        possibility_left = (
            x + direction_x >= 0 and x + direction_x <= 7
            and y - 1 >= 0
            and self.board[x + (direction_x * 1)][y - 1].piece is None
        )

        move_right = (
            destination[0] == self.board[x + (direction_x * 1)][y + 1].x
            and destination[1] == self.board[x + (direction_x * 1)][y + 1].y
        )

        move_left = (
            destination[0] == self.board[x + (direction_x * 1)][y - 1].x
            and destination[1] == self.board[x + (direction_x * 1)][y - 1].y
        )

        import pdb
        pdb.set_trace()

        if possibility_right and move_right:
            return True
        if possibility_left and move_left:
            return True
        return False
