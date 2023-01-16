import Board
from Tiles import Tiles
import Constants
import Move



class Chess():
    def __init__(self, my_side: Constants.Color) -> None:
        self.board = Board.Board()
        self.move_list = []

        self.my_side = my_side
        self.my_score = 0

        self.opp_side = Constants.Color.DARK if my_side == Constants.Color.PALE else Constants.Color.PALE
        self.opp_score = 0

    # set the board up with a specific state
    def init_board(self, state):
        self.board.apply_board_state(state)

    # show the board
    def print(self):
        # print the move list
        pass

        # print the board
        xoffset = 24
        yoffset = 24
        self.board.print(xoffset, yoffset)

    # executes my move
    def my_move(self, move: Move.Move):
        to_tile = move.get_destination()
        from_tile = self.board.get_piece_tile_for_move(move.get_piece(), self.my_side, to_tile)
        self.board.move_piece(from_tile,to_tile)
        

    # executes opponents move
    def opp_move(self, move: Move.Move):
        to_tile = move.get_destination()
        from_tile = self.board.get_piece_tile_for_move(move.get_piece(), self.opp_side, to_tile)
        self.board.move_piece(from_tile,to_tile)


