import constants


class Piece:
    def __init__(self, score, image, pos, color: constants.Color) -> None:
        self.score = score
        self.image = image
        self.pos = pos
        self.color = color



class Pawn(Piece):
    def __init__(self, pos, color: constants.Color) -> None:
        Piece.__init__(self, constants.PAWN_SCORE, "P", pos, color)

class Knight(Piece):
    def __init__(self, pos, color: constants.Color) -> None:
        Piece.__init__(self, constants.KNIGHT_SCORE, "N", pos, color)

class Bishop(Piece):
    def __init__(self, pos, color: constants.Color) -> None:
        Piece.__init__(self, constants.BISHOP_SCORE, "B", pos, color)

class Rook(Piece):
    def __init__(self, pos, color: constants.Color) -> None:
        Piece.__init__(self, constants.ROOK_SCORE, "R", pos, color)

class Queen(Piece):
    def __init__(self, pos, color: constants.Color) -> None:
        Piece.__init__(self, constants.QUEEN_SCORE, "Q", pos, color)

class King(Piece):
    def __init__(self, pos, color: constants.Color) -> None:
        Piece.__init__(self, constants.KING_SCORE, "K", pos, color)

class Empty(Piece):
    def __init__(self) -> None:
        Piece.__init__(self, constants.EMPTY_SCORE, "", (-1,-1), constants.Color.NONE)









