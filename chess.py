import pygame
import pygame.freetype
import Board
import Constants



class Chess():
    def __init__(self, my_side: Constants.Color) -> None:
        self.board = Board.Board()
        self.my_side = my_side
        self.move_list = []

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
    def my_move(self, move):
        pass

    # executes opponents move
    def opp_move(self, move):
        pass


