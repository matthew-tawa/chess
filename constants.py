from enum import Enum

# piece colors
class Color(Enum):
    NONE = -1
    PALE = 0
    DARK = 1

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

# colors        R    G    B
COLOR_WHITE  = (255, 255, 255)
COLOR_BLACK  = (0  , 0  , 0)
COLOR_GREEN  = (22 , 111, 0)
COLOR_YELLOW = (255, 204, 0)







