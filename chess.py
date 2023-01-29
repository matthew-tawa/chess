import Board
from Tiles import Tiles
import Pieces
import Constants
import Config
import Move
import Display
import math



class Chess():
    def __init__(self, my_side: Constants.Color) -> None:
        self.board = Board.Board()
        self.move_list = []
        self.promotion_flag = False

        self.my_side = my_side
        self.my_score = 0

        self.opp_side = Constants.Color.DARK if my_side == Constants.Color.PALE else Constants.Color.PALE
        self.opp_score = 0

        # for showing taken pieces
        self.pale_pieces_taken = []
        self.dark_pieces_taken = []

        # for highlighting the last moves tiles
        self.last_move = None

    # set the board up with a specific state
    def init_board(self, state):
        self.board.apply_board_state(state)

    # show the board
    def print(self):
        # print the move list
        start_x = 264
        start_y = 5
        for i, move in enumerate(self.move_list):
            y = start_y + (i - i%2)*12
            x_line_num =  start_x + math.floor(y/Config.WINDOW_SIZE_Y)*100
            x_move_pale = start_x + math.floor(y/Config.WINDOW_SIZE_Y)*100 + 20
            x_move_dark = start_x + math.floor(y/Config.WINDOW_SIZE_Y)*100 + 20 + (i%2)*50

            if i%2 == 0:
                line_num_str = str(int(i/2) + 1) + "."
                Display.render_to_screen(x_line_num, y, line_num_str, Config.COLOR_TEXT)

            Display.render_to_screen(x_move_pale if i%2 == 0 else x_move_dark, y, str(move), Config.COLOR_TEXT)
            
        # print the board
        xoffset = 24
        yoffset = 24
        self.board.print(self.last_move, xoffset, yoffset)

    # executes my move
    # move   -> my move to execute
    # return -> True if move succeeded (valid move), False otherwise
    def my_move(self, move: Move.Move) -> bool:
        if move.castle_k:
            self.last_move = (Tiles.E1, Tiles.G1) if self.my_side == Constants.Color.PALE else (Tiles.E8, Tiles.G8)
            return self.board.castle_king_side(self.my_side)
        elif move.castle_q:
            self.last_move = (Tiles.E1, Tiles.C1) if self.my_side == Constants.Color.PALE else (Tiles.E8, Tiles.C8)
            return self.board.castle_queen_side(self.my_side)
        else:
            to_tile = move.destination
            from_tile = self.board.get_piece_tile_for_move(move.get_piece(), self.my_side, to_tile, move.file_or_rank if move.ambiguous else None)

            self.last_move = (from_tile, to_tile)

            if from_tile != Tiles.NOWHERE and self.board.move_piece(from_tile,to_tile):
                self.move_list.append(move)
                return True

            return False




    # executes opponents move
    # move   -> opponents move to execute
    # return -> True if move succeeded (valid move), False otherwise
    def opp_move(self, move: Move.Move) -> bool:
        if move.castle_k:
            self.last_move = (Tiles.E1, Tiles.G1) if self.opp_side == Constants.Color.PALE else (Tiles.E8, Tiles.G8)
            return self.board.castle_king_side(self.opp_side)
        elif move.castle_q:
            self.last_move = (Tiles.E1, Tiles.C1) if self.opp_side == Constants.Color.PALE else (Tiles.E8, Tiles.C8)
            return self.board.castle_queen_side(self.opp_side)
        else:
            to_tile = move.destination
            from_tile = self.board.get_piece_tile_for_move(move.get_piece(), self.opp_side, to_tile)

            self.last_move = (from_tile, to_tile)

            if from_tile != Tiles.NOWHERE and self.board.move_piece(from_tile,to_tile):
                self.move_list.append(move)
                return True

        return False

    # return -> True if opposing king is in check, False otherwise
    def opp_king_in_check(self) -> bool:
        tiles_covered = set()
        tile_opp_king = None

        for tile in self.board.board:
            if self.board.board[tile].color != self.my_side and self.board.board[tile].__class__.__name__.lower() == "king":
                tile_opp_king = tile
            elif self.board.board[tile].color == self.my_side:
                for covered in self.board.board[tile].valid_moves:
                    tiles_covered.add(covered)
                
        return tile_opp_king in tiles_covered

    # return -> True if opposing king is in checkmate, False otherwise
    def opp_king_in_checkmate(self) -> bool:
        tiles_covered = set()
        tile_opp_king = None

        for tile in self.board.board:
            if self.board.board[tile].color != self.my_side and self.board.board[tile].__class__.__name__.lower() == "king":
                tile_opp_king = tile
            elif self.board.board[tile].color == self.my_side:
                for covered in self.board.board[tile].valid_moves:
                    tiles_covered.append(covered)
                
        return tile_opp_king in tiles_covered



    # return -> True if my king is in checkmate, False otherwise
    def my_king_in_checkmate(self) -> bool:
        tiles_covered = []
        tile_my_king = None

        for tile in self.board.board:
            if self.board.board[tile].color == self.my_side and self.board.board[tile].__class__.__name__.lower() == "king":
                tile_my_king = tile
            elif self.board.board[tile].color != self.my_side:
                for covered in self.board.board[tile].valid_moves:
                    tiles_covered.append(covered)
                
        return tile_my_king in tiles_covered
    
    
    # promotes a pawn to another piece
    # tile  -> Tile that the pawn is being promoted at
    # piece -> 1 letter string of the piece to promote to
    def promote(self, tile: Tiles, piece_str: str):
        piece = Pieces.Empty()

        if piece_str == "N":
            piece = Pieces.Knight(tile, self.board.board[tile].color)
        elif piece_str == "B":
            piece = Pieces.Bishop(tile, self.board.board[tile].color)
        elif piece_str == "R":
            piece = Pieces.Rook(tile, self.board.board[tile].color)
        elif piece_str == "Q":
            piece = Pieces.Queen(tile, self.board.board[tile].color)

        piece.has_moved = True

        self.board.promote(tile, piece)



