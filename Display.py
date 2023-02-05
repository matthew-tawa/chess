import pygame
import pygame.freetype
import Config



# fonts
font_menu = pygame.freetype.Font('font\Roboto-Regular.ttf', 14)
font_game = pygame.freetype.Font('font\Roboto-Regular.ttf', 24)


# the TextInputVisualizer needs a pygame.font type, not a pygame.freetype, so need to create it
font_input = pygame.font.Font('font\Roboto-Regular.ttf', 14)

# create the screen
screen = pygame.display.set_mode((Config.WINDOW_SIZE_X, Config.WINDOW_SIZE_Y))
pygame.display.set_caption("chess")


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
    