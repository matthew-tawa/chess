import Constants


class Piece:
    def __init__(self, score, image, pos, color: Constants.Color) -> None:
        self.score = score
        self.image = image
        self.pos = pos
        self.color = color
        self.has_moved = False



class Pawn(Piece):
    def __init__(self, pos, color: Constants.Color) -> None:
        Piece.__init__(self, Constants.PAWN_SCORE, "P", pos, color)

class Knight(Piece):
    def __init__(self, pos, color: Constants.Color) -> None:
        Piece.__init__(self, Constants.KNIGHT_SCORE, "N", pos, color)

class Bishop(Piece):
    def __init__(self, pos, color: Constants.Color) -> None:
        Piece.__init__(self, Constants.BISHOP_SCORE, "B", pos, color)

class Rook(Piece):
    def __init__(self, pos, color: Constants.Color) -> None:
        Piece.__init__(self, Constants.ROOK_SCORE, "R", pos, color)

class Queen(Piece):
    def __init__(self, pos, color: Constants.Color) -> None:
        Piece.__init__(self, Constants.QUEEN_SCORE, "Q", pos, color)

class King(Piece):
    def __init__(self, pos, color: Constants.Color) -> None:
        Piece.__init__(self, Constants.KING_SCORE, "K", pos, color)

class Empty(Piece):
    def __init__(self) -> None:
        Piece.__init__(self, Constants.EMPTY_SCORE, "", (-1,-1), Constants.Color.NONE)









