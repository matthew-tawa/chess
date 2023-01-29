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
        
        tiles_checked = []

        potential_pos = None
        while potential_pos != Tiles.NOWHERE:
            add_to_get_next_tile = 8 if potential_pos != None and potential_pos.value+8<64 else -55
            potential_pos = self.get_next_piece_position(piece, color, Tiles(potential_pos.value+add_to_get_next_tile) if potential_pos!=None else None)
            
            if potential_pos not in tiles_checked:
                tiles_checked.append(potential_pos)
                if end_pos in self.board[potential_pos].valid_moves:
                    file = self.board[potential_pos].file()
                    rank = self.board[potential_pos].rank()
                    
                    if file_or_rank != None and (file_or_rank == file or file_or_rank == rank):
                        break   # file_or_rank not None, and condition succeeds
                    elif file_or_rank == None:
                        break   # file_or_rank is None, no disambiguation needed
            else:
                potential_pos = Tiles.NOWHERE

        return potential_pos


        

    # move a piece from once position to another
    # from_tile -> tile to move from
    # to_tile   -> tile to move to
    # return    -> True if move executed, False if move not executed
    def move_piece(self, from_tile: Tiles, to_tile: Tiles, check_valid_moves: bool = True) -> bool:
        if check_valid_moves and to_tile not in self.board[from_tile].valid_moves:
            return False    
            
        self.board[to_tile] = self.board[from_tile]
        self.board[from_tile] = Pieces.Empty()
        
        self.board[to_tile].pos = to_tile
        self.board[to_tile].has_moved = True

        self.evaluate_moves()
        return True
        
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

    # manage castling king side
    def castle_king_side(self, side: Constants.Color) -> bool:
        if not self.__valid_castle("king", side):
            return False

        # move rook
        self.move_piece(\
                Tiles.H1 if side == Constants.Color.PALE else Tiles.H8,\
                Tiles.F1 if side == Constants.Color.PALE else Tiles.F8,\
                False
        )
        
        # move king
        self.move_piece(\
                Tiles.E1 if side == Constants.Color.PALE else Tiles.E8,\
                Tiles.G1 if side == Constants.Color.PALE else Tiles.G8,\
                False
        )
        return True
        


    # manage castling queen side
    def castle_queen_side(self, side: Constants.Color) -> bool:
        if not self.__valid_castle("queen", side):
            return False

        # move rook
        self.move_piece(\
                Tiles.A1 if side == Constants.Color.PALE else Tiles.A8,\
                Tiles.D1 if side == Constants.Color.PALE else Tiles.D8,\
                False
        )

        # move king
        self.move_piece(\
                Tiles.E1 if side == Constants.Color.PALE else Tiles.E8,\
                Tiles.C1 if side == Constants.Color.PALE else Tiles.C8,\
                False
        )
        return True


    # ***** CASTLING RULES *****
    # 1. king and rook may not have moved before
    # 2. all spaces between king and rook are empty
    # 3. king is not currently in check
    # 4. no tile the king passes through, or lands on, may be in check

    # evaluates whether the player can castle on the given side
    # return -> True if the caslte move is valid, False otherwise
    def __valid_castle(self, castle_side, player_side: Constants.Color) -> bool:
        tile_k = tile_b = tile_n = tile_r = tile_q = Tiles.NOWHERE
        if castle_side == "king":
            tile_k = Tiles.E1 if player_side == Constants.Color.PALE else Tiles.E8
            tile_b = Tiles.F1 if player_side == Constants.Color.PALE else Tiles.F8
            tile_n = Tiles.G1 if player_side == Constants.Color.PALE else Tiles.G8
            tile_r = Tiles.H1 if player_side == Constants.Color.PALE else Tiles.H8
        elif castle_side == "queen":
            tile_k = Tiles.E1 if player_side == Constants.Color.PALE else Tiles.E8
            tile_b = Tiles.C1 if player_side == Constants.Color.PALE else Tiles.C8
            tile_n = Tiles.B1 if player_side == Constants.Color.PALE else Tiles.B8
            tile_r = Tiles.A1 if player_side == Constants.Color.PALE else Tiles.A8
            tile_q = Tiles.D1 if player_side == Constants.Color.PALE else Tiles.D8

        # check rule 1
        if self.board[tile_r].__class__.__name__.lower() != "rook" or self.board[tile_k].__class__.__name__.lower() != "king":
            return False

        if self.board[tile_k].has_moved or self.board[tile_r].has_moved:
            return False
        
        # check rule 2
        if not self.board[tile_b].is_empty() or not self.board[tile_n].is_empty():
            return False
        
        # check rule 3 and 4
        tiles_covered = set()
        for tile in self.board:
            if self.board[tile].color != player_side:
                for covered in self.board[tile].valid_moves:
                    tiles_covered.add(covered)

        cannot_castle = tile_k in tiles_covered or tile_b in tiles_covered or \
            tile_n in tiles_covered or tile_r in tiles_covered or tile_q in tiles_covered
        
        if cannot_castle:
            return False
        else:
            return True
        

    # promotes a pawn to another piece
    # tile  -> Tile that the pawn is being promoted at
    # piece -> 1 letter string of the piece to promote to
    def promote(self, tile: Tiles, piece: Pieces):
        self.board[tile] = piece
    

    # print the board to the screen
    # print_surface -> surface to print to
    def print(self, last_move = None, xoffset = 0, yoffset = 0) -> None:
        tile_width = 24 # unit is pixels

        # printing board
        for tile in self.board:
            row_num = tile.value % 8
            col_num = math.floor(tile.value / 8)

            if last_move != None and tile in last_move:
                color_tile = Config.COLOR_CURSOR
            else:
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
            Display.render_to_screen(letter[0], letter[1], chr(letter[2]+64), Config.COLOR_TEXT)
        
        for number in number_coords:
            Display.render_to_screen(number[0], number[1], str(number[2]), Config.COLOR_TEXT)
    



import Pieces