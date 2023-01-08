import pygame as pg

# *** README
# this config file determines key bindings and other
# general settings. When changing key bindings, ens-
# ure to use the pg.K_? where ? is the desired key.
# ***

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
WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 800
WINDOW_BACKGROUND_COLOR = (0, 0, 0) # R G B