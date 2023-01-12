import pygame
import pygame.freetype
import pygame_textinput
import Config
import server
import client
import Chess
import Constants

# initialize pygame
pygame.init()

# globals
font_menu = pygame.freetype.Font('font\Roboto-Regular.ttf', 14)
font_game = pygame.freetype.Font('font\Roboto-Regular.ttf', 24)

# create the screen
screen = pygame.display.set_mode((Config.WINDOW_SIZE_X, Config.WINDOW_SIZE_Y))
pygame.display.set_caption("chess")

# initializations
def main():
    global screen, font_menu, font_game
    
    # just for displaying a board, wont be the real playing board
    c = Chess.Chess(Constants.Color.NONE)

    user_input = ""

    running = True
    while running:
        update_display_pre(c)

        font_menu.render_to(screen, (0, 250), "1- Host a game", Config.COLOR_TEXT)
        font_menu.render_to(screen, (0, 275), "2- Join a game", Config.COLOR_TEXT)

        # call event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYUP:
                handle_menu_keypress(event.key)

        
        update_display_post()


# if you want to update the display, call this function, perform your code, then call update_display_post()
def update_display_pre(c: Chess.Chess = None):
    screen.fill(Config.COLOR_WINDOW_BACKGROUND)

    if c != None:
        # display the board because it looks nice :)
        c.print_board(screen, font_menu)

# if you want to update the display, call update_display_pre(), perform your code, then call this function
def update_display_post():
    pygame.display.update()


# handles when a key is pressed in a menu
def handle_menu_keypress(key):
    match key:
        case pygame.K_1:
            ip, port = get_hosting_information()
            s = server.Server(ip ,port)
            s.start_server()
            s.game_loop()
        case pygame.K_2:
            ip, port = get_hosting_information()
            c = client.Client(ip, port)
            c.join_server()
            c.game_loop()
        case _:
            pass
    
    return

# returns the ip address and port number
# return -> (ip, port) as tuple
def get_hosting_information() -> tuple[str, str]:
    ip = get_user_input("Enter IPv4 address...")
    port = int(get_user_input("Enter Port number (>1024)..."))
    return (ip, port)

# function used to get one string from user
# prompt -> prompt to disply to user
def get_user_input(prompt: str) -> str:
    global font_menu

    # the TextInputVisualizer needs a pygame.font type, not a pygame.freetype, so need to create it
    font_input = pygame.font.Font('font\Roboto-Regular.ttf', 14)

    textinput = pygame_textinput.TextInputVisualizer(None, font_input, True, Config.COLOR_TEXT, 300, 3, Config.COLOR_TEXT)

    result = ""
    user_typing = True
    while user_typing:
        update_display_pre()

        font_menu.render_to(screen, (5, 5), prompt, Config.COLOR_TEXT)

        events = pygame.event.get()
        textinput.update(events)
        screen.blit(textinput.surface, (5,25))

        # need to check if user clicked enter
        for event in events:
            match event.type:
                case pygame.QUIT:
                    exit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        result = textinput.value
                        user_typing = False

        update_display_post()
    
    return result


    





main()
pygame.quit()