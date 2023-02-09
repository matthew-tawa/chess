import pygame
import pygame.freetype
import Config
import random
import Constants

# main game clock
clock = pygame.time.Clock()


# fonts
font_menu = pygame.freetype.Font('font\Roboto-Regular.ttf', 14)
font_game = pygame.freetype.Font('font\Roboto-Regular.ttf', 24)


# the TextInputVisualizer needs a pygame.font type, not a pygame.freetype, so need to create it
font_input = pygame.font.Font('font\Roboto-Regular.ttf', 14)

# create the screen
screen = pygame.display.set_mode((Config.WINDOW_SIZE_X, Config.WINDOW_SIZE_Y))
pygame.display.set_caption("chess")

# load a random chess piece as the icon
rand_int = random.randint(1,12)
icon_str = None

if rand_int == 1:
    icon_str = Constants.IMAGE_BISHOP_DARK
elif rand_int == 2:
    icon_str = Constants.IMAGE_BISHOP_PALE
elif rand_int == 3:
    icon_str = Constants.IMAGE_KING_DARK
elif rand_int == 4:
    icon_str = Constants.IMAGE_KING_PALE
elif rand_int == 5:
    icon_str = Constants.IMAGE_KNIGHT_DARK
elif rand_int == 6:
    icon_str = Constants.IMAGE_KNIGHT_PALE
elif rand_int == 7:
    icon_str = Constants.IMAGE_PAWN_DARK
elif rand_int == 8:
    icon_str = Constants.IMAGE_PAWN_PALE
elif rand_int == 9:
    icon_str = Constants.IMAGE_QUEEN_DARK
elif rand_int == 10:
    icon_str = Constants.IMAGE_QUEEN_PALE
elif rand_int == 11:
    icon_str = Constants.IMAGE_ROOK_DARK
elif rand_int == 12:
    icon_str = Constants.IMAGE_ROOK_PALE

icon = pygame.image.load(icon_str)
pygame.display.set_icon(icon)


# update screen size
def set_screen_size(x, y):
    global screen
    screen = pygame.display.set_mode((x, y))

# USED FOR CHESS CLASS
# adapts screen size to latest move_list length
# returns True if screen size was changed, False otherwise
current_move_list_columns = 1
def adapt_screen_size(move_list_num_cols) -> bool:
    global current_move_list_columns
    if move_list_num_cols != current_move_list_columns and move_list_num_cols > 0:
        set_screen_size(Config.WINDOW_SIZE_X + 150*move_list_num_cols, Config.WINDOW_SIZE_Y)
        current_move_list_columns = move_list_num_cols
        return True
    
    return False

# if you want to update the display, call this function, perform your code, then call update_display_post()
def update_display_pre():
    screen.fill(Config.COLOR_WINDOW_BACKGROUND)

# if you want to update the display, call update_display_pre(), perform your code, then call this function
def update_display_post():
    pygame.display.update()

# render text to the screen
def render_to_screen(x, y, string, color):
    font_menu.render_to(screen, (x, y), string, color)

# blit surface to screen
def blit_to_screen(x, y, surface):
    if surface != None:
        screen.blit(surface, (x, y))

# draws a square colord tile to the screen
def draw_tile(color, x, y, width):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, width))
    