import pygame as pg
import Constants

# ***** README
# This config file determines key bindings and other
# general settings. 
# When changing key bindings, ensure to use the pg.K_? 
# where ? is the desired key.
# When changing colors, can use any colors from the 
# Constants file, or define your own as a tuple: (R,G,B)
# *****

# strokes for pieces
KEY_CYCLE_PAWNS     = pg.K_p
KEY_CYCLE_KNIGHT    = pg.K_n
KEY_CYCLE_BISHOP    = pg.K_b
KEY_CYCLE_ROOK      = pg.K_r
KEY_CYCLE_QUEEN     = pg.K_q
KEY_CYCLE_KING      = pg.K_k

# commands
KEY_FLIP_BOARD      = pg.K_f

# window size (in pixels)
WINDOW_SIZE_X = 400
WINDOW_SIZE_Y = 400

# game element colors
COLOR_WINDOW_BACKGROUND = Constants.COLOR_BLACK
COLOR_PALE_TILE  = Constants.COLOR_WHITE
COLOR_DARK_TILE  = Constants.COLOR_GREEN
COLOR_PALE_PIECE = Constants.COLOR_YELLOW
COLOR_DARK_PIECE = Constants.COLOR_BLACK