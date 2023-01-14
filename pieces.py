import pygame
import Display
import Constants
import math
from Tiles import Tiles


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

    # prints the piece
    def print(self, x, y):
        if self.image != None:
            image = pygame.image.load(self.image)
            image = pygame.transform.scale(image, (20, 20))
            Display.blit_to_screen(x, y, image)





class Pawn(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.PAWN_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self, enemy_front_left: bool, enemy_front_right: bool):
        self.valid_moves.clear()
        self.valid_moves.append(self.pos + 8)

        if self.has_moved == False:
            self.valid_moves.append(self.pos + 16)
        
        if enemy_front_left:
            pass

        if enemy_front_right:
            pass


class Knight(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.KNIGHT_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self):
        self.valid_moves.clear()

        for tile in Tiles:
            move1 = abs(tile.value - self.pos.value) == 15
            move2 = abs(tile.value - self.pos.value) == 17
            move3 = abs(tile.value - self.pos.value) == 10
            move4 = abs(tile.value - self.pos.value) == 6

            if move1 or move2 or move3 or move4:
                self.valid_moves.append(tile)



class Bishop(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.BISHOP_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self):
        self.valid_moves.clear()

        for tile in Tiles:
            same_diag_tl_br = abs(tile.value - self.pos.value) % 9 == 0
            same_diag_bl_tr = abs(tile.value - self.pos.value) % 7 == 0

            if same_diag_tl_br or same_diag_bl_tr:
                self.valid_moves.append(tile)



class Rook(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.ROOK_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self):
        self.valid_moves.clear()

        for tile in Tiles:
            same_rank = math.floor(tile.value / 8) == math.floor(self.pos.value / 8)
            same_file = tile.value % 8 == self.pos.value % 8

            if same_rank or same_file:
                self.valid_moves.append(tile)



class Queen(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.QUEEN_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self):
        self.valid_moves.clear()

        for tile in Tiles:
            same_rank = math.floor(tile.value / 8) == math.floor(self.pos.value / 8)
            same_file = tile.value % 8 == self.pos.value % 8
            same_diag_tl_br = abs(tile.value - self.pos.value) % 9 == 0
            same_diag_bl_tr = abs(tile.value - self.pos.value) % 7 == 0

            if same_diag_tl_br or same_diag_bl_tr or same_rank or same_file:
                self.valid_moves.append(tile)



class King(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.KING_SCORE, pale_piece, dark_piece, pos, color)

    def evaluate_valid_moves(self):
        self.valid_moves.clear()

        for tile in Tiles:
            same_rank = abs(tile.value - self.pos.value) == 1
            same_file = abs(tile.value - self.pos.value) == 8
            same_diag_tl_br = abs(tile.value - self.pos.value) == 9
            same_diag_bl_tr = abs(tile.value - self.pos.value) == 7

            if same_diag_tl_br or same_diag_bl_tr or same_rank or same_file:
                self.valid_moves.append(tile)



class Empty(Piece):
    def __init__(self) -> None:
        Piece.__init__(self, Constants.EMPTY_SCORE, None, None, (-1,-1), Constants.Color.NONE)









