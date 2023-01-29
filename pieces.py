import pygame
import Display
import Constants
import math
from Tiles import Tiles
import Board

# *****************************************************************************************************
# PIECE - class to hold all basic piece information
# *****************************************************************************************************
class Piece:
    def __init__(self, score, image_pale, image_dark, pos: Tiles, color: Constants.Color) -> None:
        self.score = score
        self.__image_pale = image_pale
        self.__image_dark = image_dark
        self.image = self.__image_pale if color == Constants.Color.PALE else self.__image_dark if color == Constants.Color.DARK else None
        self.pos = pos
        self.color = color
        self.has_moved = False

        self.valid_moves = []

    # return the pieces file
    def file(self) -> str:
        return chr(65 + self.pos.value%8)

    # return the pieces rank
    def rank(self) -> str:
        return  8 - math.floor(self.pos.value/8)

    # prints the piece
    def print(self, x, y):
        if self.image != None:
            image = pygame.image.load(self.image)
            image = pygame.transform.scale(image, (20, 20))
            Display.blit_to_screen(x, y, image)

    # checks if piece is an empty piece
    def is_empty(self) -> bool:
        return self.__class__.__name__.lower() == "empty"




# *****************************************************************************************************
# PAWN - class to hold pawn information
# *****************************************************************************************************
class Pawn(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_DARK
        Piece.__init__(self, Constants.PAWN_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self, board: Board.Board):
        self.valid_moves.clear()

        pawn_on_enemy_last_rank = self.pos.value > 55 if self.color == Constants.Color.DARK else self.pos.value < 8
        if pawn_on_enemy_last_rank:
            # no valid moves (pawn about to be promoted)
            return

        direction = 1 if self.color == Constants.Color.DARK else -1

        tile_fwd_one = Tiles(self.pos.value + direction*8) if (self.pos.value + direction*8) > -1 and (self.pos.value + direction*8) < 64 else None
        tile_fwd_two = Tiles(self.pos.value + direction*16) if self.has_moved == False else None
        tile_eat_fwd_right = Tiles(self.pos.value + direction*7)
        tile_eat_fwd_left = Tiles(self.pos.value + direction*9)

        # normal forward movement of 1 tile
        if tile_fwd_one != None and board.board[tile_fwd_one].is_empty(): 
            self.valid_moves.append(tile_fwd_one)
            
            if self.has_moved == False and tile_fwd_two != None and board.board[tile_fwd_two].is_empty():
                self.valid_moves.append(tile_fwd_two)

        # special movement of eating an enemy
        if board.board[tile_eat_fwd_right].color != self.color and not board.board[tile_eat_fwd_right].is_empty():
            self.valid_moves.append(tile_eat_fwd_right)
        
        if board.board[tile_eat_fwd_left].color != self.color and not board.board[tile_eat_fwd_left].is_empty():
            self.valid_moves.append(tile_eat_fwd_left)

        

# *****************************************************************************************************
# KNIGHT - class to hold knight information
# *****************************************************************************************************
class Knight(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_KNIGHT_PALE
        dark_piece = Constants.IMAGE_KNIGHT_DARK
        Piece.__init__(self, Constants.KNIGHT_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self, board: Board.Board):
        self.valid_moves.clear()

        for tile in Tiles: 
            if tile != Tiles.NOWHERE and board.board[tile].color != self.color:
                move1 = abs(tile.value - self.pos.value) == 15
                move2 = abs(tile.value - self.pos.value) == 17
                move3 = abs(tile.value - self.pos.value) == 10
                move4 = abs(tile.value - self.pos.value) == 6

                if move1 or move2 or move3 or move4:
                    self.valid_moves.append(tile)


# *****************************************************************************************************
# BISHOP - class to hold bishop information
# *****************************************************************************************************
class Bishop(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_BISHOP_PALE
        dark_piece = Constants.IMAGE_BISHOP_DARK
        Piece.__init__(self, Constants.BISHOP_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self, board: Board.Board):
        self.valid_moves.clear()
        
        tiles_fwd = [tile for tile in Tiles if tile != Tiles.NOWHERE]
        tiles_rev = [tile for tile in reversed(Tiles) if tile != Tiles.NOWHERE]

        # top left to bishop
        # \
        #  \
        #   B
        for tile in tiles_rev:
            same_diag_tl_bishop = abs(tile.value - self.pos.value) % 9 == 0 and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_tl_bishop and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)
            
                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # bishop to bottom right
        # B
        #  \
        #   \
        for tile in tiles_fwd:
            same_diag_bishop_br = abs(tile.value - self.pos.value) % 9 == 0 and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_bishop_br and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # bottom left to bishop
        #   B
        #  /
        # /  
        for tile in tiles_fwd:
            same_diag_bl_bishop = abs(tile.value - self.pos.value) % 7 == 0 and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_bl_bishop and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # bishop to top right
        #   /
        #  /
        # B 
        for tile in tiles_rev:
            same_diag_bishop_tr = abs(tile.value - self.pos.value) % 7 == 0 and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_bishop_tr and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break


# *****************************************************************************************************
# ROOK - class to hold rook information
# *****************************************************************************************************
class Rook(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_ROOK_PALE
        dark_piece = Constants.IMAGE_ROOK_DARK
        Piece.__init__(self, Constants.ROOK_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self, board: Board.Board):
        self.valid_moves.clear()

        #with board.board as b:
        tiles_fwd = [tile for tile in Tiles if tile != Tiles.NOWHERE]
        tiles_rev = [tile for tile in reversed(Tiles) if tile != Tiles.NOWHERE]

        # top to rook
        #  |
        #  |
        #  R
        for tile in tiles_rev:
            same_file_top_rook = tile.value % 8 == self.pos.value % 8 and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_file_top_rook and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)
            
                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # rook to bottom
        #  R
        #  |
        #  |
        for tile in tiles_fwd:
            same_file_rook_bot = tile.value % 8 == self.pos.value % 8 and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_file_rook_bot and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # left to rook
        #   
        # - - R
        #   
        for tile in tiles_fwd:
            same_rank_left_rook = math.floor(tile.value / 8) == math.floor(self.pos.value / 8) and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_rank_left_rook and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # rook to right
        #   
        # R - -
        # 
        for tile in tiles_rev:
            same_rank_rook_right = math.floor(tile.value / 8) == math.floor(self.pos.value / 8) and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_rank_rook_right and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break


# *****************************************************************************************************
# QUEEN - class to hold queen information
# *****************************************************************************************************
class Queen(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_QUEEN_PALE
        dark_piece = Constants.IMAGE_QUEEN_DARK
        Piece.__init__(self, Constants.QUEEN_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self, board: Board.Board):
        self.valid_moves.clear()

        tiles_fwd = [tile for tile in Tiles if tile != Tiles.NOWHERE]
        tiles_rev = [tile for tile in reversed(Tiles) if tile != Tiles.NOWHERE]

        # top left to queen
        # \
        #  \
        #   Q
        for tile in tiles_rev:
            same_diag_tl_queen = abs(tile.value - self.pos.value) % 9 == 0 and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_tl_queen and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)
            
                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # queen to bottom right
        # Q
        #  \
        #   \
        for tile in tiles_fwd:
            same_diag_queen_br = abs(tile.value - self.pos.value) % 9 == 0 and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_queen_br and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # bottom left to queen
        #   Q
        #  /
        # /  
        for tile in tiles_fwd:
            same_diag_bl_queen = abs(tile.value - self.pos.value) % 7 == 0 and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_bl_queen and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # queen to top right
        #   /
        #  /
        # Q
        for tile in tiles_rev:
            same_diag_queen_tr = abs(tile.value - self.pos.value) % 7 == 0 and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_diag_queen_tr and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # top to queen
        #  |
        #  |
        #  Q
        for tile in tiles_rev:
            same_file_top_queen = tile.value % 8 == self.pos.value % 8 and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_file_top_queen and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)
            
                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # queen to bottom
        #  Q
        #  |
        #  |
        for tile in tiles_fwd:
            same_file_queen_bot = tile.value % 8 == self.pos.value % 8 and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_file_queen_bot and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # left to queen
        #   
        # - - Q
        #   
        for tile in tiles_fwd:
            same_rank_left_queen = math.floor(tile.value / 8) == math.floor(self.pos.value / 8) and tile.value < self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_rank_left_queen and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break

        # queen to right
        #   
        # Q - -
        # 
        for tile in tiles_rev:
            same_rank_queen_right = math.floor(tile.value / 8) == math.floor(self.pos.value / 8) and tile.value > self.pos.value
            tile_empty_or_enemy = board.board[tile].color != self.color
            
            if same_rank_queen_right and tile != self.pos:
                if tile_empty_or_enemy:
                    self.valid_moves.append(tile)

                # if we reach a populated tile, after adding it or not, we cant continue
                if not board.board[tile].is_empty():
                    break


# *****************************************************************************************************
# KING - class to hold king information
# *****************************************************************************************************
class King(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_KING_PALE
        dark_piece = Constants.IMAGE_KING_DARK
        Piece.__init__(self, Constants.KING_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self, board: Board.Board):
        self.valid_moves.clear()

        opp_king_range = self.__tiles_covered_by_opposing_king(board)

        for tile in Tiles:
            same_rank = abs(tile.value - self.pos.value) == 1
            same_file = abs(tile.value - self.pos.value) == 8
            same_diag_tl_br = abs(tile.value - self.pos.value) == 9
            same_diag_bl_tr = abs(tile.value - self.pos.value) == 7

            # if tile is within 1 of king and its either empty or opposing color
            if (same_diag_tl_br or same_diag_bl_tr or same_rank or same_file) and board.board[tile].color != self.color:
                # make sure the tile would not put king in check
                if not self.__tile_gives_check(board, tile) and tile not in opp_king_range:
                    self.valid_moves.append(tile)
    
    def __tiles_covered_by_opposing_king(self, board: Board.Board):
        opp_king_pos = None

        for tile in board.board:
            if board.board[tile].__class__.__name__.lower() == "king" and tile != self.pos:
                opp_king_pos = tile
                break
        
        # get all the tiles the opposing king can reach
        opp_king_range = [Tiles(opp_king_pos.value + x + y*8) for x in range(-1,2) for y in range(-1,2) if (x!=0 or y!=0) and (opp_king_pos.value + x + y*8)<64 and (opp_king_pos.value + x + y*8)>-1]

        return set(opp_king_range)


    # board -> the current chess board
    # tile  -> tile to check for check
    # return -> True if the given tile is covered by at least one opposing piece, False otherwise 
    def __tile_gives_check(self, board: Board.Board, tile_to_check: Tiles) -> bool:
        for tile in board.board:
            # if tile is an opposing piece
            if board.board[tile].color != self.color and not board.board[tile].is_empty():
                # check for the desired tile in the pieces valid moves
                if tile_to_check in board.board[tile].valid_moves:
                    return True

        return False

    # return -> True if king is currently in check, False otherwise
    #def currently_in_check(self, board: Board.Board) -> bool:
    #    for tile in board.board:
    #        if board.board[tile].color != self.color and self.pos in board.board[tile].valid_moves:
    #            return True
    #
    #    return False

            


# *****************************************************************************************************
# EMPTY - class to represent an empty tile
# *****************************************************************************************************
class Empty(Piece):
    def __init__(self) -> None:
        Piece.__init__(self, Constants.EMPTY_SCORE, None, None, (-1,-1), Constants.Color.NONE)
    
    def evaluate_valid_moves(self, board: Board.Board):
        pass









