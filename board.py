import pygame
import pygame.freetype
import math
import Constants
import Config
from Tiles import Tiles
import Pieces

class Board:
    def __init__(self) -> None:
        # creating board of empty Pieces

        self.board = {t: Pieces.Empty() for t in Tiles if t != Tiles.NOWHERE}
        self.flipped = False


    # takes in a board state and sets the board up
    def apply_board_state(self, state) -> None:
        for tile in state:
            p = Pieces.Empty()
            piece, color_str = state[tile].split(":")
            color = Constants.Color.DARK if color_str == "dark" else Constants.Color.PALE

            match piece:
                case "pawn":
                    p = Pieces.Pawn(tile, color)
                case "knight":
                    p = Pieces.Knight(tile, color)
                case "bishop":
                    p = Pieces.Bishop(tile, color)
                case "rook":
                    p = Pieces.Rook(tile, color)
                case "queen":
                    p = Pieces.Queen(tile, color)
                case "king":
                    p = Pieces.King(tile, color)
                case _:
                    # unrecognized piece
                    print("BOARD STATE CONTAINED AN UNRECOGNIZED PIECE")
                    pass

            self.board[tile] = p

    # returns the position of the next piece of a given type. Next piece is 
    # ordered left-right, up-down
    # takes into account rotation of board so that from player view, always 
    # works as intended (left-right, up-down)
    # piece     -> string with name of piece to search for (pawn, knight, bishop, rook, queen, king, empty)
    # start_pos -> position on board to start searching from
    def get_next_piece_position(self, piece: str, color: Constants.Color, start_pos: Tiles = None):
        # start pos depends on direction of board if not given
        if start_pos == None:
            start_pos = Tiles.H1 if self.flipped else Tiles.A8

        start_col = start_pos.value % 8
        start_row = math.floor(start_pos.value / 8)

        for it_col in range(start_col, 8+start_col):
            for it_row in range(start_row, 8+start_row):
                 # to wrap around once
                row = it_row%8
                col = (it_col + math.floor(it_row/8))%8

                # valid square to check, create tile number
                current_tile = Tiles(row*8 + col)

                if (self.board[current_tile].color != color):
                    continue # if color isnt the same as player, dont care

                if (self.board[current_tile].__class__.__name__.lower() == piece.lower()):
                    return current_tile

        # piece not on board
        return Tiles.NOWHERE
        

    # move a piece from once position to another
    def move_piece(self, from_tile: Tiles, to_tile: Tiles):
        pass

        

    # print the board to the screen
    # print_surface -> surface to print to
    def print(self, print_surface: pygame.surface, print_font: pygame.freetype, xoffset = 0, yoffset = 0) -> None:
        # printing board
        for tile in self.board:
            row_num = tile.value % 8
            col_num = math.floor(tile.value / 8)
            text = self.board[tile].image
            color_piece = Config.COLOR_DARK_PIECE if self.board[tile].color == Constants.Color.DARK else Config.COLOR_PALE_PIECE
            color_tile = Config.COLOR_DARK_TILE if ((col_num+row_num)%2) == (not self.flipped) else Config.COLOR_PALE_TILE

            x = (row_num if (not self.flipped) else (7-row_num)) * 24 + xoffset
            y = (col_num if (not self.flipped) else (7-col_num)) * 24 + yoffset

            pygame.draw.rect(print_surface, color_tile, pygame.Rect(x, y, 24, 24))
            print_font.render_to(print_surface, (x, y), text, color_piece)
        
        # printing coordinates
        letter_coords = [(x,y, x if not self.flipped else 9-x) for y in range(0,10,9) for x in range(1,9) ]
        number_coords = [(x,y, (9-y) if not self.flipped else y) for x in range(0,10,9) for y in range(1,9) ]

        letter_coords = [(x*24, y*24, z) for (x,y,z) in letter_coords]
        number_coords = [(x*24, y*24, z) for (x,y,z) in number_coords]
        
        for letter in letter_coords:
            print_font.render_to(print_surface, (letter[0], letter[1]), chr(letter[2]+64), Config.COLOR_TEXT)
        
        for number in number_coords:
            print_font.render_to(print_surface, (number[0], number[1]), str(number[2]) , Config.COLOR_TEXT)
    