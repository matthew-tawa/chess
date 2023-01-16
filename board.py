import math
import Constants
import Config
from Tiles import Tiles
import Display

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

    # piece -> string of the piece to search for
    # color -> color of the piece to find
    # rank_or_file -> used as disambiguation in case multiple of piece can make the move
    # return -> the tile of the valid piece, or NOWHERE if no piece matches criteria
    def get_piece_tile_for_move(self, piece: str, color: Constants.Color, end_pos: Tiles, file_or_rank = None):
        self.evaluate_moves()
        
        potential_pos = None
        while potential_pos != Tiles.NOWHERE:
            potential_pos = self.get_next_piece_position(piece, color, Tiles(potential_pos.value+1) if potential_pos!=None else None)
            temp_piece = self.board[potential_pos]
            temp_bool = end_pos in temp_piece.valid_moves
            if temp_bool:
                file = self.board[potential_pos].file()
                rank = self.board[potential_pos].rank()
                
                if file_or_rank != None and (file_or_rank == file or file_or_rank == rank):
                    break   # file_or_rank not None, and condition succeeds
                elif file_or_rank == None:
                    break   # file_or_rank is None, no disambiguation needed

        return potential_pos


        

    # move a piece from once position to another
    # from_tile -> tile to move from
    # to_tile   -> tile to move to
    # return    -> True if move executed, False if move not executed
    def move_piece(self, from_tile: Tiles, to_tile: Tiles) -> bool:
        if to_tile not in self.board[from_tile].valid_moves:
            return False    
            
        self.board[to_tile] = self.board[from_tile]
        self.board[from_tile] = Pieces.Empty()
        self.board[to_tile].pos = to_tile
        
    # cycle through all pieces on board and evaluate the pieces moves
    def evaluate_moves(self):
        # calculate everything except the king, then do king and check for checks
        for tile in self.board:
            if not self.board[tile].is_empty() and self.board[tile].__class__.__name__.lower() != "king":
                self.board[tile].evaluate_valid_moves(self)

        # calculate the kings
        for tile in self.board:
            if self.board[tile].__class__.__name__.lower() == "king":
                self.board[tile].evaluate_valid_moves(self)
        


        

    # print the board to the screen
    # print_surface -> surface to print to
    def print(self, xoffset = 0, yoffset = 0) -> None:
        tile_width = 24 # unit is pixels

        # printing board
        for tile in self.board:
            row_num = tile.value % 8
            col_num = math.floor(tile.value / 8)
            color_tile = Config.COLOR_DARK_TILE if ((col_num+row_num)%2) == (not self.flipped) else Config.COLOR_PALE_TILE

            x = (row_num if (not self.flipped) else (7-row_num)) * tile_width + xoffset
            y = (col_num if (not self.flipped) else (7-col_num)) * tile_width + yoffset

            Display.draw_tile(color_tile, x, y, tile_width)
            self.board[tile].print(x, y)
        
        # printing coordinates
        # offsets to account for the width of the characters to center them in the 24x24 square
        char_offset_x = 8
        char_offset_y = 5

        letter_coords = [(x,y, x if not self.flipped else 9-x) for y in range(0,10,9) for x in range(1,9) ]
        number_coords = [(x,y, (9-y) if not self.flipped else y) for x in range(0,10,9) for y in range(1,9) ]

        letter_coords = [(x*tile_width + char_offset_x, y*tile_width + char_offset_y, z) for (x,y,z) in letter_coords]
        number_coords = [(x*tile_width + char_offset_x, y*tile_width + char_offset_y, z) for (x,y,z) in number_coords]
        
        for letter in letter_coords:
            #print_font.render_to(print_surface, (letter[0], letter[1]), chr(letter[2]+64), Config.COLOR_TEXT)
            Display.render_to_screen(letter[0], letter[1], chr(letter[2]+64), Config.COLOR_TEXT)
        
        for number in number_coords:
            #print_font.render_to(print_surface, (number[0], number[1]), str(number[2]) , Config.COLOR_TEXT)
            Display.render_to_screen(number[0], number[1], str(number[2]), Config.COLOR_TEXT)
    



import Pieces