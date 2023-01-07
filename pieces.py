import constants



class Piece:
    def __init__(self, score, image, pos) -> None:
        self.score = score
        self.image = image
        self.pos = pos



class Pawn(Piece):
    def __init__(self, pos) -> None:
        Piece.__init__(self, constants.PAWN_SCORE, "P", pos)

class Knight(Piece):
    def __init__(self, pos) -> None:
        Piece.__init__(self, constants.KNIGHT_SCORE, "N", pos)

class Bishop(Piece):
    def __init__(self, pos) -> None:
        Piece.__init__(self, constants.BISHOP_SCORE, "B", pos)

class Rook(Piece):
    def __init__(self, pos) -> None:
        Piece.__init__(self, constants.ROOK_SCORE, "R", pos)

class Queen(Piece):
    def __init__(self, pos) -> None:
        Piece.__init__(self, constants.QUEEN_SCORE, "Q", pos)

class King(Piece):
    def __init__(self, pos) -> None:
        Piece.__init__(self, constants.KING_SCORE, "K", pos)









