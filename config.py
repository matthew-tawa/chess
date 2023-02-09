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
KEY_PAWNS   = pg.K_p
KEY_KNIGHT  = pg.K_n
KEY_BISHOP  = pg.K_b
KEY_ROOK    = pg.K_r
KEY_QUEEN   = pg.K_q
KEY_KING    = pg.K_k
KEY_BACK    = pg.K_ESCAPE

# commands
KEY_FLIP_BOARD = pg.K_SPACE

# graphics
WINDOW_SIZE_X = 430 # DO NOT CHANGE THIS
WINDOW_SIZE_Y = 410 # DO NOT CHANGE THIS
FPS = 10

# game element colors
COLOR_WINDOW_BACKGROUND = Constants.COLOR_GRAY
COLOR_PALE_TILE  = Constants.COLOR_PALE_BROWN
COLOR_DARK_TILE  = Constants.COLOR_DARK_BROWN
COLOR_PALE_PIECE = Constants.COLOR_WHITE
COLOR_DARK_PIECE = Constants.COLOR_BLACK
COLOR_CURSOR     = Constants.COLOR_PALE_BLUE
COLOR_TEXT       = Constants.COLOR_WHITE