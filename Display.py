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
    