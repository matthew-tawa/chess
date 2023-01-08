from enum import Enum

# piece colors
class Color(Enum):
    NONE = -1
    WHITE = 0
    BLACK = 1

# piece scores
PAWN_SCORE      = 1
KNIGHT_SCORE    = 3
BISHOP_SCORE    = 3
ROOK_SCORE      = 5
QUEEN_SCORE     = 9
KING_SCORE      = 0
EMPTY_SCORE     = -1

# board dimensions
BOARD_X = 8
BOARD_Y = 8

# server configs
SERVER_ADDRESS  = '192.168.1.15'
SERVER_PORT     = 6969




