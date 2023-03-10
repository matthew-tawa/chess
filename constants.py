from enum import Enum
import os.path

# piece colors
class Color(Enum):
    NONE = -1
    PALE = 0
    DARK = 1

# piece images
IMAGE_PAWN_PALE   = os.path.join("images", "Chess_plt60.png")
IMAGE_PAWN_DARK   = os.path.join("images", "Chess_pdt60.png")
IMAGE_KNIGHT_PALE = os.path.join("images", "Chess_nlt60.png")
IMAGE_KNIGHT_DARK = os.path.join("images", "Chess_ndt60.png")
IMAGE_BISHOP_PALE = os.path.join("images", "Chess_blt60.png")
IMAGE_BISHOP_DARK = os.path.join("images", "Chess_bdt60.png")
IMAGE_ROOK_PALE   = os.path.join("images", "Chess_rlt60.png")
IMAGE_ROOK_DARK   = os.path.join("images", "Chess_rdt60.png")
IMAGE_QUEEN_PALE  = os.path.join("images", "Chess_qlt60.png")
IMAGE_QUEEN_DARK  = os.path.join("images", "Chess_qdt60.png")
IMAGE_KING_PALE   = os.path.join("images", "Chess_klt60.png")
IMAGE_KING_DARK   = os.path.join("images", "Chess_kdt60.png")

# piece scores
PAWN_SCORE      = 1
KNIGHT_SCORE    = 3
BISHOP_SCORE    = 3
ROOK_SCORE      = 5
QUEEN_SCORE     = 9
KING_SCORE      = 100
EMPTY_SCORE     = 0

# board dimensions
BOARD_X = 8
BOARD_Y = 8

# server configs
SERVER_ADDRESS  = '192.168.1.15'
SERVER_PORT     = 4444

# colors           R    G    B
COLOR_WHITE     = (255, 255, 255)
COLOR_BLACK     = (0  , 0  , 0)
COLOR_GREEN     = (22 , 111, 0)
COLOR_YELLOW    = (255, 204, 0)
COLOR_GRAY      = (30 , 30 , 30)
COLOR_PALE_BLUE = (204, 243, 246)
COLOR_DARK_BROWN= (210, 140, 69)
COLOR_PALE_BROWN= (255, 207, 159)







