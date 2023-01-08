import pygame
import pygame.freetype
import math
import Constants
import Config
import Tiles
import Pieces

class Board:
    def __init__(self) -> None:
        # creating board of empty Pieces
        self.board = {t: Pieces.Empty() for t in Tiles}
        self.flipped = False


    # takes in a board state and sets the board up
    def apply_board_state(self, state) -> None:
        for tile in state:
            self.board[tile] = state[tile]

    # print the board to the screen
    # print_surface -> surface to print to
    def print(self, print_surface: pygame.surface, print_font: pygame.freetype) -> None:
        for tile in self.board:
            row_num = tile.value % 8
            col_num = math.floor(tile.value / 8)
            text = self.board[tile].image
            color_piece = Config.COLOR_DARK_PIECE if self.board[tile].color == Constants.Color.DARK else Config.COLOR_PALE_PIECE
            color_tile = Config.COLOR_DARK_TILE if ((col_num+row_num)%2) == (not self.flipped) else Config.COLOR_PALE_TILE

            x = (row_num if (not self.flipped) else (7-row_num)) * 24
            y = (col_num if (not self.flipped) else (7-col_num)) * 24

            pygame.draw.rect(print_surface, color_tile, pygame.Rect(x, y, 24, 24))
            print_font.render_to(print_surface, (x, y), text, color_piece)
    


b = Board()
print(b.board[Tiles.A1])
print(b.board[Tiles.A2])
print(b.board[Tiles.A3])
print(b.board[Tiles.H5])