import pygame
import Display
import Constants
from Tiles import Tiles


class Piece:
    def __init__(self, score, image_pale, image_dark, pos, color: Constants.Color) -> None:
        self.score = score
        self.__image_pale = image_pale
        self.__image_dark = image_dark
        self.pos = pos
        self.color = color
        self.has_moved = False

        self.image = self.__image_pale if color == Constants.Color.PALE else self.__image_dark if color == Constants.Color.DARK else None

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

class Knight(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.KNIGHT_SCORE, pale_piece, dark_piece, pos, color)

class Bishop(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.BISHOP_SCORE, pale_piece, dark_piece, pos, color)

class Rook(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.ROOK_SCORE, pale_piece, dark_piece, pos, color)

class Queen(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.QUEEN_SCORE, pale_piece, dark_piece, pos, color)

class King(Piece):
    def __init__(self, pos: Tiles, color: Constants.Color) -> None:
        pale_piece = Constants.IMAGE_PAWN_PALE
        dark_piece = Constants.IMAGE_PAWN_PALE
        Piece.__init__(self, Constants.KING_SCORE, pale_piece, dark_piece, pos, color)

class Empty(Piece):
    def __init__(self) -> None:
        Piece.__init__(self, Constants.EMPTY_SCORE, None, None, (-1,-1), Constants.Color.NONE)









